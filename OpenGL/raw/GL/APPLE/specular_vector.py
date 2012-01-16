'''OpenGL extension APPLE.specular_vector

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p
EXTENSION_NAME = 'GL_APPLE_specular_vector'
_p.unpack_constants( """GL_LIGHT_MODEL_SPECULAR_VECTOR_APPLE 0x85B0""", globals())


def glInitSpecularVectorAPPLE():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
