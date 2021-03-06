"""Mock module for Sphinx autodoc."""

import ctypes.util

old_find_library = ctypes.util.find_library


def new_find_library(name):
    if 'jack' in name.lower():
        return NotImplemented
    return old_find_library(name)


# Monkey-patch ctypes to disable searching for JACK
ctypes.util.find_library = new_find_library


class Fake(object):

    NULL = NotImplemented

    JackTransportStopped = 0
    JackTransportRolling = 1
    JackTransportStarting = 3
    JackTransportNetStarting = 4

    def dlopen(self, _):
        return self


ffi = Fake()
