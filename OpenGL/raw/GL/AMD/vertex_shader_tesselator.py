'''OpenGL extension AMD.vertex_shader_tesselator

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_AMD_vertex_shader_tesselator'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_AMD_vertex_shader_tesselator',False)
_p.unpack_constants( """GL_SAMPLER_BUFFER_AMD 0x9001
GL_INT_SAMPLER_BUFFER_AMD 0x9002
GL_UNSIGNED_INT_SAMPLER_BUFFER_AMD 0x9003
GL_TESSELLATION_MODE_AMD 0x9004
GL_TESSELLATION_FACTOR_AMD 0x9005
GL_DISCRETE_AMD 0x9006
GL_CONTINUOUS_AMD 0x9007""", globals())
@_f
@_p.types(None,_cs.GLfloat)
def glTessellationFactorAMD( factor ):pass
@_f
@_p.types(None,_cs.GLenum)
def glTessellationModeAMD( mode ):pass


def glInitVertexShaderTesselatorAMD():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
