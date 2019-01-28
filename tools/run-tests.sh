#!/bin/bash
mkdir node/out -p
ln -srf ./out/ node/out/Release
(cd node && tools/test.py "$@")
