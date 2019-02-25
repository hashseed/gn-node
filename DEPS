# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

vars = {
  'build_url': 'https://chromium.googlesource.com/chromium/src/build.git',
  'build_revision': 'ebd384ac0066c979fa8fcd69b139e05407618820',

  'buildtools_url': 'https://chromium.googlesource.com/chromium/src/buildtools.git',
  'buildtools_revision': '3e50219fc4503f461b2176a9976891b28d80f9ab',

  'clang_url': 'https://chromium.googlesource.com/chromium/src/tools/clang.git',
  'clang_revision': '987f14b1d69362d837743b9807e2b14caf55688f',

  'depot_tools_url': 'https://chromium.googlesource.com/chromium/tools/depot_tools.git',
  'depot_tools_revision': '95ea36ed70541b2ad01c33656c9504b7dc6404d0',

  'googletest_url': 'https://chromium.googlesource.com/external/github.com/google/googletest.git',
  'googletest_revision': '37ae1fc5e6be26f367d76c078beabd7024fed53a',

  'icu_url': 'https://chromium.googlesource.com/chromium/deps/icu.git',
  'icu_revision': '960f195aa87acaec46e6104ec93a596da7ae0843',

  'jinja2_url': 'https://chromium.googlesource.com/chromium/src/third_party/jinja2.git',
  'jinja2_revision': 'b41863e42637544c2941b574c7877d3e1f663e25',

  'markupsafe_url': 'https://chromium.googlesource.com/chromium/src/third_party/markupsafe.git',
  'markupsafe_revision': '8f45f5cfa0009d2a70589bcda0349b8cb2b72783',

  'node_url': 'https://chromium.googlesource.com/external/github.com/v8/node.git',
  'node_revision': '7ef2a111be4e64365832e17cb0ecc4cc8860bced',

  'trace_common_url': 'https://chromium.googlesource.com/chromium/src/base/trace_event/common.git',
  'trace_common_revision' : '936ba8a963284a6b3737cf2f0474a7131073abee',

  'v8_url': 'https://chromium.googlesource.com/v8/v8.git',
  'v8_revision': 'a8a45e41213d51590a1b9b0a629afece1751555c',
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
