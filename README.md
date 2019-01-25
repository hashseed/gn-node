# gn-node
Node.js built with GN

## Instructions

### Checking out source

[Get depot_tools](https://commondatastorage.googleapis.com/chrome-infra-docs/flat/depot_tools/docs/html/depot_tools_tutorial.html#_setting_up) first.

```bash
mkdir gn-node
cd gn-node
gclient config https://github.com/hashseed/gn-node --name=src --unmanaged
gclient sync
cd src
```

### Build

```
build/install-build-deps.sh
gn gen out
ninja -C out node
```
