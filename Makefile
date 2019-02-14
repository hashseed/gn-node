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
	build/install-build-deps.sh --quick-check $(BUILDDEPS_FLAGS) ||\
	build/install-build-deps.sh $(BUILDDEPS_FLAGS)

# Generate GN configs
out/Release:
	tools/gn-gen.py out/Release

out/Debug:
	tools/gn-gen.py out/Debug --debug

# Build
.PHONY: build.Release
build.Release: out/Release
	autoninja -C $<

.PHONY:
build.Debug: out/Debug
	autoninja -C $<

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
test: cctest.Release jstest.Release\
      test-addons.Release test-node-api.Release test-js-native-api.Release

.PHONY: test_g
test_g: cctest.Debug jstest.Debug\
        test-addons.Debug test-node-api.Debug test-js-native-api.Debug

# Clean
.PHONY: clean
clean:
	rm -rf out

# Test js-native-api
.PHONY: test-js-native-api.Release
test-js-native-api.Release: build.Release
	tools/test.py --test-root out/Release/gen/node/test\
	    $(PARALLEL_ARGS) -m release js-native-api

.PHONY: test-js-native-api.Debug
test-js-native-api.Debug: build.Debug
	tools/test.py --test-root out/Debug/gen/node/test\
	    $(PARALLEL_ARGS) -m debug js-native-api

# Test node-api
.PHONY: test-node-api.Release
test-node-api.Release: build.Release
	tools/test.py --test-root out/Release/gen/node/test\
	    $(PARALLEL_ARGS) -m release node-api

# Test node-api
.PHONY: test-node-api.Debug
test-node-api.Debug: build.Debug
	tools/test.py --test-root out/Debug/gen/node/test\
	    $(PARALLEL_ARGS) -m debug node-api

# Test addons
.PHONY: test-addons.Debug
test-addons.Release: build.Release
	tools/test.py --test-root out/Release/gen/node/test\
	    $(PARALLEL_ARGS) -m release addons

.PHONY: test-addons.Debug
test-addons.Debug: build.Debug
	tools/test.py --test-root out/Debug/gen/node/test\
	    $(PARALLEL_ARGS) -m debug addons

