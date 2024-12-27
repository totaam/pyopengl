'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_VERSION_GL_4_2'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_VERSION_GL_4_2',error_checker=_errors._error_checker)
GL_ACTIVE_ATOMIC_COUNTER_BUFFERS=_C('GL_ACTIVE_ATOMIC_COUNTER_BUFFERS',0x92D9)
GL_ALL_BARRIER_BITS=_C('GL_ALL_BARRIER_BITS',0xFFFFFFFF)
GL_ATOMIC_COUNTER_BARRIER_BIT=_C('GL_ATOMIC_COUNTER_BARRIER_BIT',0x00001000)
GL_ATOMIC_COUNTER_BUFFER=_C('GL_ATOMIC_COUNTER_BUFFER',0x92C0)
GL_ATOMIC_COUNTER_BUFFER_ACTIVE_ATOMIC_COUNTERS=_C('GL_ATOMIC_COUNTER_BUFFER_ACTIVE_ATOMIC_COUNTERS',0x92C5)
GL_ATOMIC_COUNTER_BUFFER_ACTIVE_ATOMIC_COUNTER_INDICES=_C('GL_ATOMIC_COUNTER_BUFFER_ACTIVE_ATOMIC_COUNTER_INDICES',0x92C6)
GL_ATOMIC_COUNTER_BUFFER_BINDING=_C('GL_ATOMIC_COUNTER_BUFFER_BINDING',0x92C1)
GL_ATOMIC_COUNTER_BUFFER_DATA_SIZE=_C('GL_ATOMIC_COUNTER_BUFFER_DATA_SIZE',0x92C4)
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_FRAGMENT_SHADER=_C('GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_FRAGMENT_SHADER',0x92CB)
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_GEOMETRY_SHADER=_C('GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_GEOMETRY_SHADER',0x92CA)
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_TESS_CONTROL_SHADER=_C('GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_TESS_CONTROL_SHADER',0x92C8)
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_TESS_EVALUATION_SHADER=_C('GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_TESS_EVALUATION_SHADER',0x92C9)
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_VERTEX_SHADER=_C('GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_VERTEX_SHADER',0x92C7)
GL_ATOMIC_COUNTER_BUFFER_SIZE=_C('GL_ATOMIC_COUNTER_BUFFER_SIZE',0x92C3)
GL_ATOMIC_COUNTER_BUFFER_START=_C('GL_ATOMIC_COUNTER_BUFFER_START',0x92C2)
GL_BUFFER_UPDATE_BARRIER_BIT=_C('GL_BUFFER_UPDATE_BARRIER_BIT',0x00000200)
GL_COMMAND_BARRIER_BIT=_C('GL_COMMAND_BARRIER_BIT',0x00000040)
GL_COMPRESSED_RGBA_BPTC_UNORM=_C('GL_COMPRESSED_RGBA_BPTC_UNORM',0x8E8C)
GL_COMPRESSED_RGB_BPTC_SIGNED_FLOAT=_C('GL_COMPRESSED_RGB_BPTC_SIGNED_FLOAT',0x8E8E)
GL_COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT=_C('GL_COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT',0x8E8F)
GL_COMPRESSED_SRGB_ALPHA_BPTC_UNORM=_C('GL_COMPRESSED_SRGB_ALPHA_BPTC_UNORM',0x8E8D)
GL_COPY_READ_BUFFER_BINDING=_C('GL_COPY_READ_BUFFER_BINDING',0x8F36)
GL_COPY_WRITE_BUFFER_BINDING=_C('GL_COPY_WRITE_BUFFER_BINDING',0x8F37)
GL_ELEMENT_ARRAY_BARRIER_BIT=_C('GL_ELEMENT_ARRAY_BARRIER_BIT',0x00000002)
GL_FRAMEBUFFER_BARRIER_BIT=_C('GL_FRAMEBUFFER_BARRIER_BIT',0x00000400)
GL_IMAGE_1D=_C('GL_IMAGE_1D',0x904C)
GL_IMAGE_1D_ARRAY=_C('GL_IMAGE_1D_ARRAY',0x9052)
GL_IMAGE_2D=_C('GL_IMAGE_2D',0x904D)
GL_IMAGE_2D_ARRAY=_C('GL_IMAGE_2D_ARRAY',0x9053)
GL_IMAGE_2D_MULTISAMPLE=_C('GL_IMAGE_2D_MULTISAMPLE',0x9055)
GL_IMAGE_2D_MULTISAMPLE_ARRAY=_C('GL_IMAGE_2D_MULTISAMPLE_ARRAY',0x9056)
GL_IMAGE_2D_RECT=_C('GL_IMAGE_2D_RECT',0x904F)
GL_IMAGE_3D=_C('GL_IMAGE_3D',0x904E)
GL_IMAGE_BINDING_ACCESS=_C('GL_IMAGE_BINDING_ACCESS',0x8F3E)
GL_IMAGE_BINDING_FORMAT=_C('GL_IMAGE_BINDING_FORMAT',0x906E)
GL_IMAGE_BINDING_LAYER=_C('GL_IMAGE_BINDING_LAYER',0x8F3D)
GL_IMAGE_BINDING_LAYERED=_C('GL_IMAGE_BINDING_LAYERED',0x8F3C)
GL_IMAGE_BINDING_LEVEL=_C('GL_IMAGE_BINDING_LEVEL',0x8F3B)
GL_IMAGE_BINDING_NAME=_C('GL_IMAGE_BINDING_NAME',0x8F3A)
GL_IMAGE_BUFFER=_C('GL_IMAGE_BUFFER',0x9051)
GL_IMAGE_CUBE=_C('GL_IMAGE_CUBE',0x9050)
GL_IMAGE_CUBE_MAP_ARRAY=_C('GL_IMAGE_CUBE_MAP_ARRAY',0x9054)
GL_IMAGE_FORMAT_COMPATIBILITY_BY_CLASS=_C('GL_IMAGE_FORMAT_COMPATIBILITY_BY_CLASS',0x90C9)
GL_IMAGE_FORMAT_COMPATIBILITY_BY_SIZE=_C('GL_IMAGE_FORMAT_COMPATIBILITY_BY_SIZE',0x90C8)
GL_IMAGE_FORMAT_COMPATIBILITY_TYPE=_C('GL_IMAGE_FORMAT_COMPATIBILITY_TYPE',0x90C7)
GL_INT_IMAGE_1D=_C('GL_INT_IMAGE_1D',0x9057)
GL_INT_IMAGE_1D_ARRAY=_C('GL_INT_IMAGE_1D_ARRAY',0x905D)
GL_INT_IMAGE_2D=_C('GL_INT_IMAGE_2D',0x9058)
GL_INT_IMAGE_2D_ARRAY=_C('GL_INT_IMAGE_2D_ARRAY',0x905E)
GL_INT_IMAGE_2D_MULTISAMPLE=_C('GL_INT_IMAGE_2D_MULTISAMPLE',0x9060)
GL_INT_IMAGE_2D_MULTISAMPLE_ARRAY=_C('GL_INT_IMAGE_2D_MULTISAMPLE_ARRAY',0x9061)
GL_INT_IMAGE_2D_RECT=_C('GL_INT_IMAGE_2D_RECT',0x905A)
GL_INT_IMAGE_3D=_C('GL_INT_IMAGE_3D',0x9059)
GL_INT_IMAGE_BUFFER=_C('GL_INT_IMAGE_BUFFER',0x905C)
GL_INT_IMAGE_CUBE=_C('GL_INT_IMAGE_CUBE',0x905B)
GL_INT_IMAGE_CUBE_MAP_ARRAY=_C('GL_INT_IMAGE_CUBE_MAP_ARRAY',0x905F)
GL_MAX_ATOMIC_COUNTER_BUFFER_BINDINGS=_C('GL_MAX_ATOMIC_COUNTER_BUFFER_BINDINGS',0x92DC)
GL_MAX_ATOMIC_COUNTER_BUFFER_SIZE=_C('GL_MAX_ATOMIC_COUNTER_BUFFER_SIZE',0x92D8)
GL_MAX_COMBINED_ATOMIC_COUNTERS=_C('GL_MAX_COMBINED_ATOMIC_COUNTERS',0x92D7)
GL_MAX_COMBINED_ATOMIC_COUNTER_BUFFERS=_C('GL_MAX_COMBINED_ATOMIC_COUNTER_BUFFERS',0x92D1)
GL_MAX_COMBINED_IMAGE_UNIFORMS=_C('GL_MAX_COMBINED_IMAGE_UNIFORMS',0x90CF)
GL_MAX_COMBINED_IMAGE_UNITS_AND_FRAGMENT_OUTPUTS=_C('GL_MAX_COMBINED_IMAGE_UNITS_AND_FRAGMENT_OUTPUTS',0x8F39)
GL_MAX_FRAGMENT_ATOMIC_COUNTERS=_C('GL_MAX_FRAGMENT_ATOMIC_COUNTERS',0x92D6)
GL_MAX_FRAGMENT_ATOMIC_COUNTER_BUFFERS=_C('GL_MAX_FRAGMENT_ATOMIC_COUNTER_BUFFERS',0x92D0)
GL_MAX_FRAGMENT_IMAGE_UNIFORMS=_C('GL_MAX_FRAGMENT_IMAGE_UNIFORMS',0x90CE)
GL_MAX_GEOMETRY_ATOMIC_COUNTERS=_C('GL_MAX_GEOMETRY_ATOMIC_COUNTERS',0x92D5)
GL_MAX_GEOMETRY_ATOMIC_COUNTER_BUFFERS=_C('GL_MAX_GEOMETRY_ATOMIC_COUNTER_BUFFERS',0x92CF)
GL_MAX_GEOMETRY_IMAGE_UNIFORMS=_C('GL_MAX_GEOMETRY_IMAGE_UNIFORMS',0x90CD)
GL_MAX_IMAGE_SAMPLES=_C('GL_MAX_IMAGE_SAMPLES',0x906D)
GL_MAX_IMAGE_UNITS=_C('GL_MAX_IMAGE_UNITS',0x8F38)
GL_MAX_TESS_CONTROL_ATOMIC_COUNTERS=_C('GL_MAX_TESS_CONTROL_ATOMIC_COUNTERS',0x92D3)
GL_MAX_TESS_CONTROL_ATOMIC_COUNTER_BUFFERS=_C('GL_MAX_TESS_CONTROL_ATOMIC_COUNTER_BUFFERS',0x92CD)
GL_MAX_TESS_CONTROL_IMAGE_UNIFORMS=_C('GL_MAX_TESS_CONTROL_IMAGE_UNIFORMS',0x90CB)
GL_MAX_TESS_EVALUATION_ATOMIC_COUNTERS=_C('GL_MAX_TESS_EVALUATION_ATOMIC_COUNTERS',0x92D4)
GL_MAX_TESS_EVALUATION_ATOMIC_COUNTER_BUFFERS=_C('GL_MAX_TESS_EVALUATION_ATOMIC_COUNTER_BUFFERS',0x92CE)
GL_MAX_TESS_EVALUATION_IMAGE_UNIFORMS=_C('GL_MAX_TESS_EVALUATION_IMAGE_UNIFORMS',0x90CC)
GL_MAX_VERTEX_ATOMIC_COUNTERS=_C('GL_MAX_VERTEX_ATOMIC_COUNTERS',0x92D2)
GL_MAX_VERTEX_ATOMIC_COUNTER_BUFFERS=_C('GL_MAX_VERTEX_ATOMIC_COUNTER_BUFFERS',0x92CC)
GL_MAX_VERTEX_IMAGE_UNIFORMS=_C('GL_MAX_VERTEX_IMAGE_UNIFORMS',0x90CA)
GL_MIN_MAP_BUFFER_ALIGNMENT=_C('GL_MIN_MAP_BUFFER_ALIGNMENT',0x90BC)
GL_NUM_SAMPLE_COUNTS=_C('GL_NUM_SAMPLE_COUNTS',0x9380)
GL_PACK_COMPRESSED_BLOCK_DEPTH=_C('GL_PACK_COMPRESSED_BLOCK_DEPTH',0x912D)
GL_PACK_COMPRESSED_BLOCK_HEIGHT=_C('GL_PACK_COMPRESSED_BLOCK_HEIGHT',0x912C)
GL_PACK_COMPRESSED_BLOCK_SIZE=_C('GL_PACK_COMPRESSED_BLOCK_SIZE',0x912E)
GL_PACK_COMPRESSED_BLOCK_WIDTH=_C('GL_PACK_COMPRESSED_BLOCK_WIDTH',0x912B)
GL_PIXEL_BUFFER_BARRIER_BIT=_C('GL_PIXEL_BUFFER_BARRIER_BIT',0x00000080)
GL_SHADER_IMAGE_ACCESS_BARRIER_BIT=_C('GL_SHADER_IMAGE_ACCESS_BARRIER_BIT',0x00000020)
GL_TEXTURE_FETCH_BARRIER_BIT=_C('GL_TEXTURE_FETCH_BARRIER_BIT',0x00000008)
GL_TEXTURE_IMMUTABLE_FORMAT=_C('GL_TEXTURE_IMMUTABLE_FORMAT',0x912F)
GL_TEXTURE_UPDATE_BARRIER_BIT=_C('GL_TEXTURE_UPDATE_BARRIER_BIT',0x00000100)
GL_TRANSFORM_FEEDBACK_ACTIVE=_C('GL_TRANSFORM_FEEDBACK_ACTIVE',0x8E24)
GL_TRANSFORM_FEEDBACK_BARRIER_BIT=_C('GL_TRANSFORM_FEEDBACK_BARRIER_BIT',0x00000800)
GL_TRANSFORM_FEEDBACK_PAUSED=_C('GL_TRANSFORM_FEEDBACK_PAUSED',0x8E23)
GL_UNIFORM_ATOMIC_COUNTER_BUFFER_INDEX=_C('GL_UNIFORM_ATOMIC_COUNTER_BUFFER_INDEX',0x92DA)
GL_UNIFORM_BARRIER_BIT=_C('GL_UNIFORM_BARRIER_BIT',0x00000004)
GL_UNPACK_COMPRESSED_BLOCK_DEPTH=_C('GL_UNPACK_COMPRESSED_BLOCK_DEPTH',0x9129)
GL_UNPACK_COMPRESSED_BLOCK_HEIGHT=_C('GL_UNPACK_COMPRESSED_BLOCK_HEIGHT',0x9128)
GL_UNPACK_COMPRESSED_BLOCK_SIZE=_C('GL_UNPACK_COMPRESSED_BLOCK_SIZE',0x912A)
GL_UNPACK_COMPRESSED_BLOCK_WIDTH=_C('GL_UNPACK_COMPRESSED_BLOCK_WIDTH',0x9127)
GL_UNSIGNED_INT_ATOMIC_COUNTER=_C('GL_UNSIGNED_INT_ATOMIC_COUNTER',0x92DB)
GL_UNSIGNED_INT_IMAGE_1D=_C('GL_UNSIGNED_INT_IMAGE_1D',0x9062)
GL_UNSIGNED_INT_IMAGE_1D_ARRAY=_C('GL_UNSIGNED_INT_IMAGE_1D_ARRAY',0x9068)
GL_UNSIGNED_INT_IMAGE_2D=_C('GL_UNSIGNED_INT_IMAGE_2D',0x9063)
GL_UNSIGNED_INT_IMAGE_2D_ARRAY=_C('GL_UNSIGNED_INT_IMAGE_2D_ARRAY',0x9069)
GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE=_C('GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE',0x906B)
GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE_ARRAY=_C('GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE_ARRAY',0x906C)
GL_UNSIGNED_INT_IMAGE_2D_RECT=_C('GL_UNSIGNED_INT_IMAGE_2D_RECT',0x9065)
GL_UNSIGNED_INT_IMAGE_3D=_C('GL_UNSIGNED_INT_IMAGE_3D',0x9064)
GL_UNSIGNED_INT_IMAGE_BUFFER=_C('GL_UNSIGNED_INT_IMAGE_BUFFER',0x9067)
GL_UNSIGNED_INT_IMAGE_CUBE=_C('GL_UNSIGNED_INT_IMAGE_CUBE',0x9066)
GL_UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY=_C('GL_UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY',0x906A)
GL_VERTEX_ATTRIB_ARRAY_BARRIER_BIT=_C('GL_VERTEX_ATTRIB_ARRAY_BARRIER_BIT',0x00000001)
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLint,_cs.GLboolean,_cs.GLint,_cs.GLenum,_cs.GLenum)
def glBindImageTexture(unit,texture,level,layered,layer,access,format):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLuint)
def glDrawArraysInstancedBaseInstance(mode,first,count,instancecount,baseinstance):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p,_cs.GLsizei,_cs.GLuint)
def glDrawElementsInstancedBaseInstance(mode,count,type,indices,instancecount,baseinstance):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p,_cs.GLsizei,_cs.GLint,_cs.GLuint)
def glDrawElementsInstancedBaseVertexBaseInstance(mode,count,type,indices,instancecount,basevertex,baseinstance):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLsizei)
def glDrawTransformFeedbackInstanced(mode,id,instancecount):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLsizei)
def glDrawTransformFeedbackStreamInstanced(mode,id,stream,instancecount):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetActiveAtomicCounterBufferiv(program,bufferIndex,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLsizei,arrays.GLintArray)
def glGetInternalformativ(target,internalformat,pname,count,params):pass
@_f
@_p.types(None,_cs.GLbitfield)
def glMemoryBarrier(barriers):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLsizei)
def glTexStorage1D(target,levels,internalformat,width):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,_cs.GLsizei)
def glTexStorage2D(target,levels,internalformat,width,height):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei)
def glTexStorage3D(target,levels,internalformat,width,height,depth):pass
