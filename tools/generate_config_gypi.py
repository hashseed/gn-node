# Copyright (c) 2013-2019 GitHub Inc.
# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import re
import os
import subprocess
import sys

root_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(root_dir, "node", "tools"))
import getmoduleversion

GN_RE = re.compile(r'(\w+)\s+=\s+(.*?)$', re.MULTILINE)

def bool_string_to_number(v):
  return 1 if v == "true" else 0

def string_to_number(v):
  return int(v)

def translate_config(config):
  if sys.platform == "darwin":
    shlib_suffix = "dylib"
  else:
    shlib_suffix = "so"

  return {
    "target_defaults": {
      "default_configuration": "Debug" if config["is_debug"] else "Release",
    },
    "variables": {
      "node_module_version": string_to_number(config["node_module_version"]),
      "node_report": config["node_report"],
      "node_shared": bool_string_to_number(config["is_component_build"]),
      "node_code_cache_path":
          "node_code_cache.cc" if config["node_use_code_cache"] else "",
      "shlib_suffix": shlib_suffix,
      # v8_enable_inspector is actually a misnomer, and only affects node.
      "v8_enable_inspector":
          bool_string_to_number(config["node_enable_inspector"]),
      "v8_enable_i18n_support":
          bool_string_to_number(config["v8_enable_i18n_support"]),
      # introduced for building addons.
      "node_use_openssl": config["node_use_openssl"],
      "build_v8_with_gn": "false",
      "enable_lto": "false",
      "openssl_fips": "",
    }
  }

def main(jinja_dir, gn_out_dir, output_file, depfile):
  # Get GN config and parse into a dictionary.
  gnconfig = subprocess.check_output(
                 ["gn", "args", "--list", "--short", "-C", gn_out_dir])
  config = dict(re.findall(GN_RE, gnconfig))
  config["node_module_version"] = getmoduleversion.get_version()

  # Write output.
  with open(output_file, "w") as f:
    f.write(repr(translate_config(config)))

  # Write depfile. Force regenerating config.gypi when GN configs change.
  with open(depfile, "w") as f:
    dot_gn = os.path.abspath(os.path.join(root_dir, ".gn"))
    args_gn = os.path.abspath(os.path.join(gn_out_dir, "args.gn"))
    if not os.path.exists(args_gn):
      # Do not depend on args.gn if it does not exist.
      args_gn = ""
    f.write("%s: %s %s" %(output_file, dot_gn, args_gn))

if __name__ == '__main__':
  main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
