# gn-node
Node.js built with GN

## Background
V8 was originally built with SCons. Following Chromium, it made the switch to GYP, completing in around 2012. That was when Node.js started its success story. However, again following Chromium, V8 made the switch to GN, completing in 2016. So far, Node.js has hesitated in adopting GN. One of the reasons is its now established native modules ecosystem that relies on GYP for build configuration.

Electron, having both Chromium and Node.js as its dependencies, adopted GN. Many files in this repository have been derived from the [Electron project](https://github.com/electron/node), with appropriate changes to avoid the need for forking files, to implement a standalone build, or fix test failures.

Some reading material:
* [GN build system](https://www.chromium.org/developers/gn-build-configuration)
* ["Build Node with GN" discussion](https://github.com/nodejs/node/issues/21410)
* [GYP deprecation and Node.js](https://docs.google.com/document/d/1gvHuesiuvLzD6X6ONddxXRxhODlOJlxgfoTNZTlKLGA/edit)
* [Bazel for Node](https://docs.google.com/document/d/101BP4BpZoP4tsMGo4j_MhoyLv169-2Oq_HeyWykCNGc/edit)

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
