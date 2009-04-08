'''OpenGL extension EXT.vertex_weighting

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.vertex_weighting to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.EXT.vertex_weighting import *
### END AUTOGENERATED SECTION