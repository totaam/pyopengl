'''OpenGL extension ARB.texture_float

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p
EXTENSION_NAME = 'GL_ARB_texture_float'
_p.unpack_constants( """GL_TEXTURE_RED_TYPE_ARB 0x8C10
GL_TEXTURE_GREEN_TYPE_ARB 0x8C11
GL_TEXTURE_BLUE_TYPE_ARB 0x8C12
GL_TEXTURE_ALPHA_TYPE_ARB 0x8C13
GL_TEXTURE_LUMINANCE_TYPE_ARB 0x8C14
GL_TEXTURE_INTENSITY_TYPE_ARB 0x8C15
GL_TEXTURE_DEPTH_TYPE_ARB 0x8C16
GL_UNSIGNED_NORMALIZED_ARB 0x8C17
GL_RGBA32F_ARB 0x8814
GL_RGB32F_ARB 0x8815
GL_ALPHA32F_ARB 0x8816
GL_INTENSITY32F_ARB 0x8817
GL_LUMINANCE32F_ARB 0x8818
GL_LUMINANCE_ALPHA32F_ARB 0x8819
GL_RGBA16F_ARB 0x881A
GL_RGB16F_ARB 0x881B
GL_ALPHA16F_ARB 0x881C
GL_INTENSITY16F_ARB 0x881D
GL_LUMINANCE16F_ARB 0x881E
GL_LUMINANCE_ALPHA16F_ARB 0x881F""", globals())


def glInitTextureFloatARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
