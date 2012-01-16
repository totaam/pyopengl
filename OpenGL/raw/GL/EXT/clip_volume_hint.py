'''OpenGL extension EXT.clip_volume_hint

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p
EXTENSION_NAME = 'GL_EXT_clip_volume_hint'
_p.unpack_constants( """GL_CLIP_VOLUME_CLIPPING_HINT_EXT 0x80F0""", globals())
glget.addGLGetConstant( GL_CLIP_VOLUME_CLIPPING_HINT_EXT, (1,) )


def glInitClipVolumeHintEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
