'''OpenGL extension SGIX.async_histogram

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p
EXTENSION_NAME = 'GL_SGIX_async_histogram'
_p.unpack_constants( """GL_ASYNC_HISTOGRAM_SGIX 0x832C
GL_MAX_ASYNC_HISTOGRAM_SGIX 0x832D""", globals())
glget.addGLGetConstant( GL_ASYNC_HISTOGRAM_SGIX, (1,) )
glget.addGLGetConstant( GL_MAX_ASYNC_HISTOGRAM_SGIX, (1,) )


def glInitAsyncHistogramSGIX():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
