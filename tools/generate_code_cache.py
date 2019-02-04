import subprocess
import sys

def main(node_exe, script, output):
  subprocess.check_output(
      [node_exe, "--expose-internals", script, output])

if __name__ == '__main__':
  main(sys.argv[1], sys.argv[2], sys.argv[3])
