# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

ifdef JOBS
  PARALLEL_ARGS = -j $(JOBS)
endif

BUILDDEPS_FLAGS = --no-nacl --no-chromeos-fonts --no-arm --lib32

# Gclient sync and check build deps
deps:
	gclient sync
	build/install-build-deps.sh --quick-check $(BUILDDEPS_FLAGS) || build/install-build-deps.sh $(BUILDDEPS_FLAGS)

# Generate GN configs
out/Release:
	gn gen $@ -q --args="is_debug = false"

out/Debug:
	gn gen $@ -q --args="is_debug = true v8_optimized_debug = true"

# Build
.PHONY: build.Release
build.Release: out/Release
	gn gen $< && autoninja -C $<

.PHONY:
build.Debug: out/Debug
	gn gen $< && autoninja -C $<

# Link node binary
node: build.Release
	if [ ! -r $@ -o ! -L $@ ]; then ln -fs out/Release/node $@; fi

node_g: build.Debug
	if [ ! -r $@ -o ! -L $@ ]; then ln -fs out/Debug/node $@; fi

# Run cctest
.PHONY: cctest.Release
cctest.Release: build.Release
	out/Release/node_cctest

.PHONY: cctest.Debug
cctest.Debug: build.Debug
	out/Debug/node_cctest

# Run JS tests
.PHONY: jstest.Release
jstest.Release: build.Release
	tools/test.py $(PARALLEL_ARGS) -m release

.PHONY: jstest.Debug
jstest.Debug: build.Debug
	tools/test.py $(PARALLEL_ARGS) -m debug

# Run all tests
.PHONY: test
test: cctest.Release jstest.Release build-addons

.PHONY: test_g
test_g: cctest.Debug jstest.Debug

# Clean
.PHONY: clean
clean:
	rm -rf out

RELEASE_NODE = $(abspath out/Release/node)
NPM_CLI = $(abspath node/deps/npm/bin/npm-cli.js)

ADDONS_BINDING_GYPS := \
	$(filter-out node/test/addons/??_*/binding.gyp, \
		$(wildcard node/test/addons/*/binding.gyp))

ADDONS_BINDING_SOURCES := \
	$(filter-out node/test/addons/??_*/*.cc, $(wildcard node/test/addons/*/*.cc)) \
	$(filter-out node/test/addons/??_*/*.h, $(wildcard node/test/addons/*/*.h))

ADDONS_PREREQS := out/Release/gen/node/js2c_inputs/config.gypi \
	node/deps/npm/node_modules/node-gyp/package.json node/tools/build-addons.js \
	node/deps/uv/include/*.h v8/include/*.h \
	node/src/node.h node/src/node_buffer.h node/src/node_object_wrap.h \
        node/src/node_version.h

NODE_DIR := $(CURDIR)/node

node/tools/doc/node_modules: node/tools/doc/package.json $(RELEASE_NODE)
	cd node/tools/doc && $(RELEASE_NODE) $(NPM_CLI) ci

out/Release/.docbuildstamp: node/tools/doc/addon-verify.js \
	node/doc/api/addons.md node/tools/doc/node_modules \
	$(RELEASE_NODE)
	rm -r node/test/addons/??_*/; \
	$(RELEASE_NODE) $< \
	touch $@;

out/Release/.addonsbuildstamp: $(ADDONS_PREREQS) \
	$(ADDONS_BINDING_GYPS) $(ADDONS_BINDING_SOURCES) \
	out/Release/.docbuildstamp
	env npm_config_loglevel=silent npm_config_nodedir="$(NODE_DIR)" \
	npm_config_python="python" $(RELEASE_NODE) $(NODE_DIR)/tools/build-addons \
  	$(NODE_DIR)/deps/npm/node_modules/node-gyp/bin/node-gyp.js \
  	$(NODE_DIR)/test/addons; \
	touch $@

.PHONY: build-addons
build-addons: out/Release/.addonsbuildstamp
