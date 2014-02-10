'''OpenGL extension SGIX.video_resize

This module customises the behaviour of the 
OpenGL.raw.GLX.SGIX.video_resize to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/SGIX/video_resize.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GLX import _types
from OpenGL.raw.GLX.SGIX.video_resize import *
from OpenGL.raw.GLX.SGIX.video_resize import _EXTENSION_NAME

def glInitVideoResizeSGIX():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION