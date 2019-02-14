# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

vars = {
  'build_url': 'https://chromium.googlesource.com/chromium/src/build.git',
  'build_revision': '2030c341b05453dd2aad584ffac3787d47d2555c',

  'buildtools_url': 'https://chromium.googlesource.com/chromium/buildtools.git',
  'buildtools_revision': '6fbda1b24c1893a893b17aa219b765b9e7c801d8',

  'clang_url': 'https://chromium.googlesource.com/chromium/src/tools/clang.git',
  'clang_revision': '1dc75416344975a4fdcc5f805985bec3d704df7d',

  'depot_tools_url': 'https://chromium.googlesource.com/chromium/tools/depot_tools.git',
  'depot_tools_revision': '61d0c292535e8e6c1102f198ec1ef47f50075ceb',

  'googletest_url': 'https://chromium.googlesource.com/external/github.com/google/googletest.git',
  'googletest_revision': '5ec7f0c4a113e2f18ac2c6cc7df51ad6afc24081',

  'icu_url': 'https://chromium.googlesource.com/chromium/deps/icu.git',
  'icu_revision': '07e7295d964399ee7bee16a3ac7ca5a053b2cf0a',

  'jinja2_url': 'https://chromium.googlesource.com/chromium/src/third_party/jinja2.git',
  'jinja2_revision': 'b41863e42637544c2941b574c7877d3e1f663e25',

  'markupsafe_url': 'https://chromium.googlesource.com/chromium/src/third_party/markupsafe.git',
  'markupsafe_revision': '8f45f5cfa0009d2a70589bcda0349b8cb2b72783',

  'node_url': 'https://chromium.googlesource.com/external/github.com/v8/node.git',
  'node_revision': 'd422eda408ee2fa72e95f4f00ea3948dcc70ae22',

  'trace_common_url': 'https://chromium.googlesource.com/chromium/src/base/trace_event/common.git',
  'trace_common_revision' : 'e31a1706337ccb9a658b37d29a018c81695c6518',

  'v8_url': 'https://chromium.googlesource.com/v8/v8.git',
  'v8_revision': '77c94fae3a1a1c0588d905f2b3afa60b5a396ecf',
}

deps = {
  'node-ci/base/trace_event/common': Var('trace_common_url') + '@' + Var('trace_common_revision'),
  'node-ci/build': Var('build_url') + '@' + Var('build_revision'),
  'node-ci/buildtools': Var('buildtools_url') + '@' + Var('buildtools_revision'),
  'node-ci/tools/clang': Var('clang_url') + '@' + Var('clang_revision'),
  'node-ci/third_party/depot_tools': Var('depot_tools_url') + '@' + Var('depot_tools_revision'),
  'node-ci/third_party/googletest/src': Var('googletest_url') + '@' + Var('googletest_revision'),
  'node-ci/third_party/icu': Var('icu_url') + '@' + Var('icu_revision'),
  'node-ci/third_party/jinja2': Var('jinja2_url') + '@' + Var('jinja2_revision'),
  'node-ci/third_party/markupsafe': Var('markupsafe_url') + '@' + Var('markupsafe_revision'),
  'node-ci/v8': Var('v8_url') + '@' +  Var('v8_revision'),
  'node-ci/node': Var('node_url') + '@' + Var('node_revision'),
}

recursedeps = [
  'node-ci/buildtools',
]

hooks = [
  {
    'name': 'clang',
    'pattern': '.',
    'action': ['python', 'node-ci/tools/clang/scripts/update.py'],
  },
  {
    'name': 'generate_node_filelist',
    'pattern': 'node-ci/node',
    'action': ['python', 'node-ci/tools/generate_node_files_json.py'],
  },
  # Pull GN using checked-in hashes.
  {
    'name': 'gn_win',
    'pattern': '.',
    'condition': 'host_os == "win"',
    'action': [ 'download_from_google_storage',
                '--no_resume',
                '--platform=win32',
                '--no_auth',
                '--bucket', 'chromium-gn',
                '-s', 'node-ci/buildtools/win/gn.exe.sha1',
    ],
  },
  {
    'name': 'gn_mac',
    'pattern': '.',
    'condition': 'host_os == "mac"',
    'action': [ 'download_from_google_storage',
                '--no_resume',
                '--platform=darwin',
                '--no_auth',
                '--bucket', 'chromium-gn',
                '-s', 'node-ci/buildtools/mac/gn.sha1',
    ],
  },
  {
    'name': 'gn_linux',
    'pattern': '.',
    'condition': 'host_os == "linux"',
    'action': [ 'download_from_google_storage',
                '--no_resume',
                '--platform=linux*',
                '--no_auth',
                '--bucket', 'chromium-gn',
                '-s', 'node-ci/buildtools/linux64/gn.sha1',
    ],
  },
  {
    'name': 'sysroot_x64',
    'pattern': '.',
    'condition': 'checkout_linux and checkout_x64',
    'action': ['python',
               'node-ci/build/linux/sysroot_scripts/install-sysroot.py',
               '--arch=x64'],
  },
]
