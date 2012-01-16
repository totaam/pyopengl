'''OpenGL extension ATI.vertex_attrib_array_object

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ATI_vertex_attrib_array_object'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ATI_vertex_attrib_array_object',False)

@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLenum,_cs.GLboolean,_cs.GLsizei,_cs.GLuint,_cs.GLuint)
def glVertexAttribArrayObjectATI( index,size,type,normalized,stride,buffer,offset ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLfloatArray)
def glGetVertexAttribArrayObjectfvATI( index,pname,params ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetVertexAttribArrayObjectivATI( index,pname,params ):pass


def glInitVertexAttribArrayObjectATI():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
