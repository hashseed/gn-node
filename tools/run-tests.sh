#!/bin/bash
set -e
out/node_cctest
mkdir node/out -p
ln -srf ./out/ node/out/Release
(cd node && tools/test.py "$@")
