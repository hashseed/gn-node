# Note: The buildbots evaluate this file with CWD set to the parent
# directory and assume that the root of the checkout is in ./v8/, so
# all paths in here must match this assumption.

vars = {
  'chromium_url': 'https://chromium.googlesource.com',
  'boringssl_git': 'https://boringssl.googlesource.com',
  'boringssl_revision': '8e8f250422663106d478f6927beefba289a95b37',
  'v8_revision': '91344c5f65fb74eac12bb25c970bf5bbb8947b09',
  'node_url': 'https://github.com/nodejs',
}

deps = {
  'src/build':
    Var('chromium_url') + '/chromium/src/build.git' + '@' + '59bf3c64e4481e765d916699cb1fc40496a5ae50',
  'src/third_party/icu':
    Var('chromium_url') + '/chromium/deps/icu.git' + '@' + '07e7295d964399ee7bee16a3ac7ca5a053b2cf0a',
  #'src/third_party/boringssl/src':
  #  Var('boringssl_git') + '/boringssl.git' + '@' +  Var('boringssl_revision'),
  'src/v8':
    Var('chromium_url') + '/v8/v8.git' + '@' +  Var('v8_revision'),
  'src/buildtools':
    Var('chromium_url') + '/chromium/buildtools.git' + '@' + '2f02e1f363b1af2715536f38e239853f04ec1497',
  'src/third_party/googletest/src':
    Var('chromium_url') + '/external/github.com/google/googletest.git' + '@' + '9518a57428ae0a7ed450c1361768e84a2a38af5a',
  'src/node':
    Var('node_url') + '/node.git' + '@' + 'f4697ba718bed0fcd1a1cebbe1a5dbe8f4893ebf',
  'src/tools/clang':
    Var('chromium_url') + '/chromium/src/tools/clang.git' + '@' + '3a16568a56486d7d032b8ec7b8dae892413a9a7a',
  'src/third_party/jinja2':
    Var('chromium_url') + '/chromium/src/third_party/jinja2.git' + '@' + 'b41863e42637544c2941b574c7877d3e1f663e25',
  'src/third_party/markupsafe':
    Var('chromium_url') + '/chromium/src/third_party/markupsafe.git' + '@' + '8f45f5cfa0009d2a70589bcda0349b8cb2b72783',
  'src/base/trace_event/common':
    Var('chromium_url') + '/chromium/src/base/trace_event/common.git' + '@' + 'e31a1706337ccb9a658b37d29a018c81695c6518',
}

recursedeps = [
  'src/buildtools',
]

hooks = [
  {
    # Note: On Win, this should run after win_toolchain, as it may use it.
    'name': 'clang',
    'pattern': '.',
    # clang not supported on aix
    'condition': 'host_os != "aix"',
    'action': ['python', 'src/tools/clang/scripts/update.py'],
  },
  {
    # Note: On Win, this should run after win_toolchain, as it may use it.
    'name': 'generate_node_filelist',
    'pattern': 'src/node',
    'action': ['python', 'src/tools/generate_gn_filenames_json.py'],
  },
]
