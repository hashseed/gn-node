# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import subprocess
import sys

def main(argv):
  stamp = argv[2]
  arg_start = 3

  # Parse env variables provided in the form `--env name value`.
  # Convert paths to absolute paths.
  env = os.environ.copy()
  while argv[arg_start] == "--env":
    value = argv[arg_start + 2]
    if os.path.exists(value):
      value = os.path.abspath(value)
    env[argv[arg_start + 1]] = value
    arg_start = arg_start + 3

  try:
    subprocess.check_output(argv[arg_start:], cwd=argv[1], env=env,
                            stderr=subprocess.STDOUT)
  except subprocess.CalledProcessError as exc:
    print(exc.output)
    raise

  with open(stamp, 'w') as file:
    file.write('stamp')

if __name__ == '__main__':
  main(sys.argv)
