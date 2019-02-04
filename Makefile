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
.PHONY:
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
.PHONY:
cctest.Release: build.Release
	out/Release/node_cctest

.PHONY:
cctest.Debug: build.Debug
	out/Debug/node_cctest

# Run JS tests
.PHONY:
jstest.Release: build.Release
	tools/test.py $(PARALLEL_ARGS) -m release

.PHONY:
jstest.Debug: build.Debug
	tools/test.py $(PARALLEL_ARGS) -m debug

# Run all tests
.PHONY:
test: cctest.Release jstest.Release 

.PHONY:
test_g: cctest.Debug jstest.Debug 

# Clean
.PHONY:
clean:
	rm -rf out
