'''OpenGL extension SGIS.texture_lod

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p
EXTENSION_NAME = 'GL_SGIS_texture_lod'
_p.unpack_constants( """GL_TEXTURE_MIN_LOD_SGIS 0x813A
GL_TEXTURE_MAX_LOD_SGIS 0x813B
GL_TEXTURE_BASE_LEVEL_SGIS 0x813C
GL_TEXTURE_MAX_LEVEL_SGIS 0x813D""", globals())


def glInitTextureLodSGIS():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
