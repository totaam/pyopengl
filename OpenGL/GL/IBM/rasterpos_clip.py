'''OpenGL extension IBM.rasterpos_clip

This module customises the behaviour of the 
OpenGL.raw.GL.IBM.rasterpos_clip to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.IBM.rasterpos_clip import *
### END AUTOGENERATED SECTION