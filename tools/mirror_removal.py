# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

# This script recursively removes files from to_dir that do not exist
# in from_dir. This is to remove outdated artifacts in incremental builds.

import os
import shutil
import sys

def mirror_removal(from_dir, to_dir, dirpath, list, remove):
 for file in list:
   if not os.path.exists(os.path.join(from_dir, dirpath, file)):
     delete_file = os.path.join(to_dir, dirpath, file)
     if os.path.exists(delete_file):
       remove(delete_file)

def main(from_dir, to_dir, stamp):
  os.chdir(to_dir)
  for dirpath, dirs, files in os.walk(".", topdown=False):
    mirror_removal(from_dir, to_dir, dirpath, files, lambda x: os.unlink(x))
    mirror_removal(from_dir, to_dir, dirpath, dirs, lambda x: shutil.rmtree(x))

  with open(stamp, 'w') as file:
    file.write('stamp')

if __name__ == '__main__':
  main(os.path.abspath(sys.argv[1]),
       os.path.abspath(sys.argv[2]),
       os.path.abspath(sys.argv[3]))
