
# Partially stolen from https://bitbucket.org/mblum/libgp/src/2537ea7329ef/.ycm_extra_conf.py
import os
import ycm_core

# These are the compilation flags that will be used in case there's no
# compilation database set (by default, one is not set).
# CHANGE THIS LIST OF FLAGS. YES, THIS IS THE DROID YOU HAVE BEEN LOOKING FOR.
flags = [
    '-x', 'c++',
    '-Wall',
    '-Wextra',
    '-Werror',
  #  '-Wno-long-long',
  #  '-Wno-variadic-macros',
  #  '-fexceptions',
    # THIS IS IMPORTANT! Without a "-std=<something>" flag, clang won't know which
    # language to use when compiling headers. So it will guess. Badly. So C++
    # headers will be compiled as C headers. You don't want that so ALWAYS specify
    # a "-std=<something>".
    # For a C project, you would set this to something like 'c99' instead of
    # 'c++11'.
    '-std=c++14',
    # ...and the same thing goes for the magic -x option which specifies the
    # language that the files to be compiled are written in. This is mostly
    # relevant for c++ headers.
    # For a C project, you would set this to 'c' instead of 'c++'.
    # This path will only work on OS X, but extra paths that don't exist are not
    # harmful
  # '-isystem', '/System/Library/Frameworks/Python.framework/Headers',
  # '-isystem', '/usr/local/include',
  # '-isystem', '/usr/local/include/eigen3',
  # '-I', 'include',
  # '-I.',
]

def FlagsForFile(filename, **kwargs):
    return {
            'flags' : flags,
    }

