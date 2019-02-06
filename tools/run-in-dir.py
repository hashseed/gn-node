# Copyright (c) 2013-2019 GitHub Inc.
# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import subprocess
import sys

def main(argv):
  cwd = argv[1]
  os.chdir(cwd)
  os.execv(sys.executable, [sys.executable] + argv[2:])

if __name__ == '__main__':
  main(sys.argv)
