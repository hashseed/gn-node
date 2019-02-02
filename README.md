# Node.js built with GN

## Background
V8 was originally built with SCons. Following Chromium, it made the switch to GYP, completing around 2012. That was when Node.js started its success story. However, again following Chromium, V8 made the switch to GN, completing in 2016. So far, Node.js has hesitated in adopting GN. One of the reasons is its now established native modules ecosystem that relies on GYP for build configuration.

Electron, having both Chromium and Node.js as its dependencies, adopted GN. Many files in this repository have been derived from the [Electron project](https://github.com/electron/node), with appropriate changes to avoid the need for forking files, to implement a standalone build, or to fix test failures.

Some reading material:
* [GN build system](https://www.chromium.org/developers/gn-build-configuration)
* [Discussion on building Node.js with GN](https://github.com/nodejs/node/issues/21410)
* [Discussion on building Node.js with cmake](https://github.com/nodejs/TSC/issues/648)
* [Discussion on building Node.js with Bazel](https://github.com/nodejs/TSC/issues/464)
* [Document on GYP deprecation and Node.js](https://docs.google.com/document/d/1gvHuesiuvLzD6X6ONddxXRxhODlOJlxgfoTNZTlKLGA/edit)
* [Document on Bazel for Node.js](https://docs.google.com/document/d/101BP4BpZoP4tsMGo4j_MhoyLv169-2Oq_HeyWykCNGc/edit)

## Instructions

### Checking out source

[Get depot_tools](https://commondatastorage.googleapis.com/chrome-infra-docs/flat/depot_tools/docs/html/depot_tools_tutorial.html#_setting_up) first.

```bash
mkdir gn-node
cd gn-node
gclient config https://github.com/hashseed/gn-node --name=src --unmanaged
cd src
```

### Build

```bash
cd src
make deps
make node
```

### Test

```bash
JOBS=4 make test
```

## Project priorities
* Stay as slim as possible. By avoiding to fork files from dependencies, future maintenance becomes less a hassle.
* Stay as up-to-date as possible. The point of this is to be able to build with newest versions of dependencies, including Node.js, V8, and ICU.
* Simplicify. It should be easy to get up and running.

## Not yet implemented
* Support building on Mac and Windows. The current configurations have only been tested for Linux.
* Platform-specific OpenSSL build configurations. The current build only supports the slowest platform-independent configuration.
* Code caching support.
* Enable shared library build.
* Optionally: support for BoringSSL.
* Support building native modules as part of testing.

## Explicit non-goals
* To translate every configuration from the GYP build.
* To support platforms not supported by Chromium.
* To replace Node.js' test runner with the one used by V8.
* To use GN to build native modules.
