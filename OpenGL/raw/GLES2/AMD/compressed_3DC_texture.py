'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES2 import _types as _cs
# End users want this...
from OpenGL.raw.GLES2._types import *
from OpenGL.raw.GLES2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLES2_AMD_compressed_3DC_texture'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLES2,'GLES2_AMD_compressed_3DC_texture',error_checker=_errors._error_checker)
GL_3DC_XY_AMD=_C('GL_3DC_XY_AMD',0x87FA)
GL_3DC_X_AMD=_C('GL_3DC_X_AMD',0x87F9)
