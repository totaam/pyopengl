'''OpenGL extension VERSION.GL_3_0_DEPRECATED

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_VERSION_GL_3_0'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_VERSION_GL_3_0',True)
_p.unpack_constants( """GL_CLAMP_VERTEX_COLOR 0x891A
GL_CLAMP_FRAGMENT_COLOR 0x891B
GL_ALPHA_INTEGER 0x8D97""", globals())


