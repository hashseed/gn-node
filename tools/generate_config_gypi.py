# TODO: assess which if any of the config variables are important to include in
# the js2c'd config.gypi.
import sys

def main(args):
  out = args[0]
  with open(out, 'w') as f:
      f.write("""
{ 'target_defaults': { 'default_configuration' : 'Release' },
  'variables': { 'v8_enable_inspector' : 1,
                 'node_report' : 0,
                 'node_shared_openssl' : 0,
                 'v8_enable_i18n_support' : 1
               }
}
""")

if __name__ == '__main__':
  main(sys.argv[1:])
