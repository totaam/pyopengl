'''OpenGL extension ARB.texture_border_clamp

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p
EXTENSION_NAME = 'GL_ARB_texture_border_clamp'
_p.unpack_constants( """GL_CLAMP_TO_BORDER_ARB 0x812D""", globals())


def glInitTextureBorderClampARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
