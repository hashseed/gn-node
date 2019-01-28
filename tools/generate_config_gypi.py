import re
import subprocess
import sys

GN_RE = re.compile(r'(\w+)\s+=\s+(.*?)$', re.MULTILINE)

def get_template_content(template_file):
  with open(template_file, "r") as f:
    return f.read()

def main(jinja_dir, gn_out_dir, template_file, output_file):
  # Get GN config and parse into a dictionary.
  gnconfig = subprocess.check_output(
                 ["gn", "args", "--list", "--short", "-C", gn_out_dir])
  config = dict(re.findall(GN_RE, gnconfig))

  # Fill in template.
  sys.path.append(jinja_dir)
  from jinja2 import Template
  template = Template(get_template_content(template_file))
  rendered_template = template.render(config)

  # Write output.
  print(rendered_template)
  with open(output_file, "w") as f:
    f.write(rendered_template)

if __name__ == '__main__':
  main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
