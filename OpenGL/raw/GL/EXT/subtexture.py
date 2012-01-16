'''OpenGL extension EXT.subtexture

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_subtexture'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_subtexture',False)

@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTexSubImage1DEXT( target,level,xoffset,width,format,type,pixels ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTexSubImage2DEXT( target,level,xoffset,yoffset,width,height,format,type,pixels ):pass


def glInitSubtextureEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
