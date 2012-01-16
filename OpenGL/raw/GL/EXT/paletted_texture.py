'''OpenGL extension EXT.paletted_texture

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_paletted_texture'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_paletted_texture',False)
_p.unpack_constants( """GL_COLOR_INDEX1_EXT 0x80E2
GL_COLOR_INDEX2_EXT 0x80E3
GL_COLOR_INDEX4_EXT 0x80E4
GL_COLOR_INDEX8_EXT 0x80E5
GL_COLOR_INDEX12_EXT 0x80E6
GL_COLOR_INDEX16_EXT 0x80E7
GL_TEXTURE_INDEX_SIZE_EXT 0x80ED""", globals())
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glColorTableEXT( target,internalFormat,width,format,type,table ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glGetColorTableEXT( target,format,type,data ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetColorTableParameterivEXT( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetColorTableParameterfvEXT( target,pname,params ):pass


def glInitPalettedTextureEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
