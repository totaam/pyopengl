'''OpenGL extension SGIX.ir_instrument1

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p
EXTENSION_NAME = 'GL_SGIX_ir_instrument1'
_p.unpack_constants( """GL_IR_INSTRUMENT1_SGIX 0x817F""", globals())


def glInitIrInstrument1SGIX():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
