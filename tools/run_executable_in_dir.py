# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import subprocess
import sys

def main(argv):
  stamp = argv[2]
  subprocess.check_output(argv[3:], cwd=argv[1])
  with open(stamp, 'w') as file:
    file.write('stamp')

if __name__ == '__main__':
  main(sys.argv)
