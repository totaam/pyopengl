'''OpenGL extension NV.parameter_buffer_object2

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p
EXTENSION_NAME = 'GL_NV_parameter_buffer_object2'



def glInitParameterBufferObject2NV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
