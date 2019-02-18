# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import subprocess
import sys

def main(node_exe, script, output):
  node_exe = os.path.abspath(node_exe)
  subprocess.check_output(
      [node_exe, '--expose-internals', script, output])

if __name__ == '__main__':
  main(sys.argv[1], sys.argv[2], sys.argv[3])
