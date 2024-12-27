'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ARB_program_interface_query'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_ARB_program_interface_query',error_checker=_errors._error_checker)
GL_ACTIVE_RESOURCES=_C('GL_ACTIVE_RESOURCES',0x92F5)
GL_ACTIVE_VARIABLES=_C('GL_ACTIVE_VARIABLES',0x9305)
GL_ARRAY_SIZE=_C('GL_ARRAY_SIZE',0x92FB)
GL_ARRAY_STRIDE=_C('GL_ARRAY_STRIDE',0x92FE)
GL_ATOMIC_COUNTER_BUFFER=_C('GL_ATOMIC_COUNTER_BUFFER',0x92C0)
GL_ATOMIC_COUNTER_BUFFER_INDEX=_C('GL_ATOMIC_COUNTER_BUFFER_INDEX',0x9301)
GL_BLOCK_INDEX=_C('GL_BLOCK_INDEX',0x92FD)
GL_BUFFER_BINDING=_C('GL_BUFFER_BINDING',0x9302)
GL_BUFFER_DATA_SIZE=_C('GL_BUFFER_DATA_SIZE',0x9303)
GL_BUFFER_VARIABLE=_C('GL_BUFFER_VARIABLE',0x92E5)
GL_COMPATIBLE_SUBROUTINES=_C('GL_COMPATIBLE_SUBROUTINES',0x8E4B)
GL_COMPUTE_SUBROUTINE=_C('GL_COMPUTE_SUBROUTINE',0x92ED)
GL_COMPUTE_SUBROUTINE_UNIFORM=_C('GL_COMPUTE_SUBROUTINE_UNIFORM',0x92F3)
GL_FRAGMENT_SUBROUTINE=_C('GL_FRAGMENT_SUBROUTINE',0x92EC)
GL_FRAGMENT_SUBROUTINE_UNIFORM=_C('GL_FRAGMENT_SUBROUTINE_UNIFORM',0x92F2)
GL_GEOMETRY_SUBROUTINE=_C('GL_GEOMETRY_SUBROUTINE',0x92EB)
GL_GEOMETRY_SUBROUTINE_UNIFORM=_C('GL_GEOMETRY_SUBROUTINE_UNIFORM',0x92F1)
GL_IS_PER_PATCH=_C('GL_IS_PER_PATCH',0x92E7)
GL_IS_ROW_MAJOR=_C('GL_IS_ROW_MAJOR',0x9300)
GL_LOCATION=_C('GL_LOCATION',0x930E)
GL_LOCATION_INDEX=_C('GL_LOCATION_INDEX',0x930F)
GL_MATRIX_STRIDE=_C('GL_MATRIX_STRIDE',0x92FF)
GL_MAX_NAME_LENGTH=_C('GL_MAX_NAME_LENGTH',0x92F6)
GL_MAX_NUM_ACTIVE_VARIABLES=_C('GL_MAX_NUM_ACTIVE_VARIABLES',0x92F7)
GL_MAX_NUM_COMPATIBLE_SUBROUTINES=_C('GL_MAX_NUM_COMPATIBLE_SUBROUTINES',0x92F8)
GL_NAME_LENGTH=_C('GL_NAME_LENGTH',0x92F9)
GL_NUM_ACTIVE_VARIABLES=_C('GL_NUM_ACTIVE_VARIABLES',0x9304)
GL_NUM_COMPATIBLE_SUBROUTINES=_C('GL_NUM_COMPATIBLE_SUBROUTINES',0x8E4A)
GL_OFFSET=_C('GL_OFFSET',0x92FC)
GL_PROGRAM_INPUT=_C('GL_PROGRAM_INPUT',0x92E3)
GL_PROGRAM_OUTPUT=_C('GL_PROGRAM_OUTPUT',0x92E4)
GL_REFERENCED_BY_COMPUTE_SHADER=_C('GL_REFERENCED_BY_COMPUTE_SHADER',0x930B)
GL_REFERENCED_BY_FRAGMENT_SHADER=_C('GL_REFERENCED_BY_FRAGMENT_SHADER',0x930A)
GL_REFERENCED_BY_GEOMETRY_SHADER=_C('GL_REFERENCED_BY_GEOMETRY_SHADER',0x9309)
GL_REFERENCED_BY_TESS_CONTROL_SHADER=_C('GL_REFERENCED_BY_TESS_CONTROL_SHADER',0x9307)
GL_REFERENCED_BY_TESS_EVALUATION_SHADER=_C('GL_REFERENCED_BY_TESS_EVALUATION_SHADER',0x9308)
GL_REFERENCED_BY_VERTEX_SHADER=_C('GL_REFERENCED_BY_VERTEX_SHADER',0x9306)
GL_SHADER_STORAGE_BLOCK=_C('GL_SHADER_STORAGE_BLOCK',0x92E6)
GL_TESS_CONTROL_SUBROUTINE=_C('GL_TESS_CONTROL_SUBROUTINE',0x92E9)
GL_TESS_CONTROL_SUBROUTINE_UNIFORM=_C('GL_TESS_CONTROL_SUBROUTINE_UNIFORM',0x92EF)
GL_TESS_EVALUATION_SUBROUTINE=_C('GL_TESS_EVALUATION_SUBROUTINE',0x92EA)
GL_TESS_EVALUATION_SUBROUTINE_UNIFORM=_C('GL_TESS_EVALUATION_SUBROUTINE_UNIFORM',0x92F0)
GL_TOP_LEVEL_ARRAY_SIZE=_C('GL_TOP_LEVEL_ARRAY_SIZE',0x930C)
GL_TOP_LEVEL_ARRAY_STRIDE=_C('GL_TOP_LEVEL_ARRAY_STRIDE',0x930D)
GL_TRANSFORM_FEEDBACK_VARYING=_C('GL_TRANSFORM_FEEDBACK_VARYING',0x92F4)
GL_TYPE=_C('GL_TYPE',0x92FA)
GL_UNIFORM=_C('GL_UNIFORM',0x92E1)
GL_UNIFORM_BLOCK=_C('GL_UNIFORM_BLOCK',0x92E2)
GL_VERTEX_SUBROUTINE=_C('GL_VERTEX_SUBROUTINE',0x92E8)
GL_VERTEX_SUBROUTINE_UNIFORM=_C('GL_VERTEX_SUBROUTINE_UNIFORM',0x92EE)
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetProgramInterfaceiv(program,programInterface,pname,params):pass
@_f
@_p.types(_cs.GLuint,_cs.GLuint,_cs.GLenum,arrays.GLcharArray)
def glGetProgramResourceIndex(program,programInterface,name):pass
@_f
@_p.types(_cs.GLint,_cs.GLuint,_cs.GLenum,arrays.GLcharArray)
def glGetProgramResourceLocation(program,programInterface,name):pass
@_f
@_p.types(_cs.GLint,_cs.GLuint,_cs.GLenum,arrays.GLcharArray)
def glGetProgramResourceLocationIndex(program,programInterface,name):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLsizei,arrays.GLsizeiArray,arrays.GLcharArray)
def glGetProgramResourceName(program,programInterface,index,bufSize,length,name):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLsizei,arrays.GLuintArray,_cs.GLsizei,arrays.GLsizeiArray,arrays.GLintArray)
def glGetProgramResourceiv(program,programInterface,index,propCount,props,count,length,params):pass
