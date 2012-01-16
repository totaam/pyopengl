'''OpenGL extension SGIS.pixel_texture

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SGIS_pixel_texture'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_SGIS_pixel_texture',False)
_p.unpack_constants( """GL_PIXEL_TEXTURE_SGIS 0x8353
GL_PIXEL_FRAGMENT_RGB_SOURCE_SGIS 0x8354
GL_PIXEL_FRAGMENT_ALPHA_SOURCE_SGIS 0x8355
GL_PIXEL_GROUP_COLOR_SGIS 0x8356""", globals())
@_f
@_p.types(None,_cs.GLenum,_cs.GLint)
def glPixelTexGenParameteriSGIS( pname,param ):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLintArray)
def glPixelTexGenParameterivSGIS( pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat)
def glPixelTexGenParameterfSGIS( pname,param ):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glPixelTexGenParameterfvSGIS( pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLintArray)
def glGetPixelTexGenParameterivSGIS( pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glGetPixelTexGenParameterfvSGIS( pname,params ):pass


def glInitPixelTextureSGIS():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
