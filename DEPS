vars = {
  'build_url': 'https://chromium.googlesource.com/chromium/src/build.git',
  'build_revision': 'a041d217401076580e70d78b6eb57dfe2678ddc8',

  'buildtools_url': 'https://chromium.googlesource.com/chromium/buildtools.git',
  'buildtools_revision': '2f02e1f363b1af2715536f38e239853f04ec1497',

  'clang_url': 'https://chromium.googlesource.com/chromium/src/tools/clang.git',
  'clang_revision': '3a16568a56486d7d032b8ec7b8dae892413a9a7a',

  'googletest_url': 'https://chromium.googlesource.com/external/github.com/google/googletest.git',
  'googletest_revision': '9518a57428ae0a7ed450c1361768e84a2a38af5a',

  'icu_url': 'https://chromium.googlesource.com/chromium/deps/icu.git',
  'icu_revision': '07e7295d964399ee7bee16a3ac7ca5a053b2cf0a',

  'jinja2_url': 'https://chromium.googlesource.com/chromium/src/third_party/jinja2.git',
  'jinja2_revision': 'b41863e42637544c2941b574c7877d3e1f663e25',

  'markupsafe_url': 'https://chromium.googlesource.com/chromium/src/third_party/markupsafe.git',
  'markupsafe_revision': '8f45f5cfa0009d2a70589bcda0349b8cb2b72783',

  'node_url': 'https://github.com/hashseed/node',
  'node_branch': 'origin/canary',

  'trace_common_url': 'https://chromium.googlesource.com/chromium/src/base/trace_event/common.git',
  'trace_common_revision' : 'e31a1706337ccb9a658b37d29a018c81695c6518',

  'v8_url': 'https://chromium.googlesource.com/v8/v8.git',
  'v8_revision': 'a1efb4134ec76f2fa60e89562dc2bf4f6a9c5c9e',
}

deps = {
  'src/base/trace_event/common': Var('trace_common_url') + '@' + Var('trace_common_revision'),
  'src/build': Var('build_url') + '@' + Var('build_revision'),
  'src/buildtools': Var('buildtools_url') + '@' + Var('buildtools_revision'),
  'src/tools/clang': Var('clang_url') + '@' + Var('clang_revision'),
  'src/third_party/googletest/src': Var('googletest_url') + '@' + Var('googletest_revision'),
  'src/third_party/icu': Var('icu_url') + '@' + Var('icu_revision'),
  'src/third_party/jinja2': Var('jinja2_url') + '@' + Var('jinja2_revision'),
  'src/third_party/markupsafe': Var('markupsafe_url') + '@' + Var('markupsafe_revision'),
  'src/v8': Var('v8_url') + '@' +  Var('v8_revision'),
  'src/node': Var('node_url') + '@' + Var('node_branch'),
}

recursedeps = [
  'src/buildtools',
]

hooks = [
  {
    'name': 'clang',
    'pattern': '.',
    'action': ['python', 'src/tools/clang/scripts/update.py'],
  },
  {
    'name': 'generate_node_filelist',
    'pattern': 'src/node',
    'action': ['python', 'src/tools/generate_node_files_json.py'],
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
                '-s', 'src/buildtools/win/gn.exe.sha1',
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
                '-s', 'src/buildtools/mac/gn.sha1',
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
                '-s', 'src/buildtools/linux64/gn.sha1',
    ],
  },
  # Pull clang-format binaries using checked-in hashes.
  {
    'name': 'clang_format_win',
    'pattern': '.',
    'condition': 'host_os == "win"',
    'action': [ 'download_from_google_storage',
                '--no_resume',
                '--platform=win32',
                '--no_auth',
                '--bucket', 'chromium-clang-format',
                '-s', 'src/buildtools/win/clang-format.exe.sha1',
    ],
  },
  {
    'name': 'clang_format_mac',
    'pattern': '.',
    'condition': 'host_os == "mac"',
    'action': [ 'download_from_google_storage',
                '--no_resume',
                '--platform=darwin',
                '--no_auth',
                '--bucket', 'chromium-clang-format',
                '-s', 'src/buildtools/mac/clang-format.sha1',
    ],
  },
  {
    'name': 'clang_format_linux',
    'pattern': '.',
    'condition': 'host_os == "linux"',
    'action': [ 'download_from_google_storage',
                '--no_resume',
                '--platform=linux*',
                '--no_auth',
                '--bucket', 'chromium-clang-format',
                '-s', 'src/buildtools/linux64/clang-format.sha1',
    ],
  },

]
