'''OpenGL extension VERSION.EGL_1_5

This module customises the behaviour of the 
OpenGL.raw.EGL.VERSION.EGL_1_5 to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/VERSION/EGL_1_5.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper

import ctypes
from OpenGL.raw.EGL import _types
from OpenGL.raw.EGL.VERSION.EGL_1_5 import *
from OpenGL.raw.EGL.VERSION.EGL_1_5 import _EXTENSION_NAME

def glInitEgl15VERSION():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION