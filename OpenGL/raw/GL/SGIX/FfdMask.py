'''OpenGL extension SGIX.FfdMask

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p
EXTENSION_NAME = 'GL_SGIX_FfdMask'
_p.unpack_constants( """GL_TEXTURE_DEFORMATION_BIT_SGIX 0x1
GL_GEOMETRY_DEFORMATION_BIT_SGIX 0x2""", globals())


def glInitFfdmaskSGIX():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
