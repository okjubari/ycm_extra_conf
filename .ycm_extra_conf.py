import os
import ycm_core


flags = [
        '-x', 'c++',
        '-Wall',
        '-Wextra',
        '-Werror',
        '-std=c++14',
        ]

def FlagsForFile(filename, **kwargs):
    return {
            'flags' : flags,
            }

