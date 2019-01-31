import re
import os
import subprocess
import sys

root_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(root_dir, "node", "tools"))
import getmoduleversion

GN_RE = re.compile(r'(\w+)\s+=\s+(.*?)$', re.MULTILINE)

def bool_to_number_filter(v):
  return 1 if v == "true" else 0

def load_template(template_file):
  with open(template_file, "r") as f:
    return f.read()

def main(jinja_dir, gn_out_dir, template_file, output_file, depfile):
  # Get GN config and parse into a dictionary.
  gnconfig = subprocess.check_output(
                 ["gn", "args", "--list", "--short", "-C", gn_out_dir])
  config = dict(re.findall(GN_RE, gnconfig))

  config["node_module_version"] = getmoduleversion.get_version()

  # Fill in template.
  sys.path.append(jinja_dir)
  from jinja2 import Environment, FunctionLoader
  env = Environment(loader=FunctionLoader(load_template),
                    trim_blocks=True, lstrip_blocks=True)
  env.filters["to_number"] = bool_to_number_filter
  template = env.get_template(template_file)
  rendered_template = template.render(config)

  # Write output.
  print(rendered_template)
  with open(output_file, "w") as f:
    f.write(rendered_template)

  # Write depfile. Force regenerating config.gypi when GN configs change.
  with open(depfile, "w") as f:
    dot_gn = os.path.abspath(os.path.join(root_dir, ".gn"))
    args_gn = os.path.abspath(os.path.join(gn_out_dir, "args.gn"))
    f.write("%s: %s %s" %(output_file, dot_gn, args_gn))

if __name__ == '__main__':
  main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
