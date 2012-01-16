'''OpenGL extension EXT.pixel_transform

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_pixel_transform'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_pixel_transform',False)
_p.unpack_constants( """GL_PIXEL_TRANSFORM_2D_EXT 0x8330
GL_PIXEL_MAG_FILTER_EXT 0x8331
GL_PIXEL_MIN_FILTER_EXT 0x8332
GL_PIXEL_CUBIC_WEIGHT_EXT 0x8333
GL_CUBIC_EXT 0x8334
GL_AVERAGE_EXT 0x8335
GL_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT 0x8336
GL_MAX_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT 0x8337
GL_PIXEL_TRANSFORM_2D_MATRIX_EXT 0x8338""", globals())
glget.addGLGetConstant( GL_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT, (1,) )
glget.addGLGetConstant( GL_MAX_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT, (1,) )
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint)
def glPixelTransformParameteriEXT( target,pname,param ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLfloat)
def glPixelTransformParameterfEXT( target,pname,param ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glPixelTransformParameterivEXT( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glPixelTransformParameterfvEXT( target,pname,params ):pass


def glInitPixelTransformEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
