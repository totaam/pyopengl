'''OpenGL extension SGIS.generate_mipmap

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p
EXTENSION_NAME = 'GL_SGIS_generate_mipmap'
_p.unpack_constants( """GL_GENERATE_MIPMAP_SGIS 0x8191
GL_GENERATE_MIPMAP_HINT_SGIS 0x8192""", globals())
glget.addGLGetConstant( GL_GENERATE_MIPMAP_HINT_SGIS, (1,) )


def glInitGenerateMipmapSGIS():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
