'''OpenGL extension SGIX.ycrcb_subsample

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p
EXTENSION_NAME = 'GL_SGIX_ycrcb_subsample'



def glInitYcrcbSubsampleSGIX():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
