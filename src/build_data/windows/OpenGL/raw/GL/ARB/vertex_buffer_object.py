'''OpenGL extension ARB.vertex_buffer_object

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_vertex_buffer_object'
_DEPRECATED = False
GL_BUFFER_SIZE_ARB = constant.Constant( 'GL_BUFFER_SIZE_ARB', 0x8764 )
GL_BUFFER_USAGE_ARB = constant.Constant( 'GL_BUFFER_USAGE_ARB', 0x8765 )
GL_ARRAY_BUFFER_ARB = constant.Constant( 'GL_ARRAY_BUFFER_ARB', 0x8892 )
GL_ELEMENT_ARRAY_BUFFER_ARB = constant.Constant( 'GL_ELEMENT_ARRAY_BUFFER_ARB', 0x8893 )
GL_ARRAY_BUFFER_BINDING_ARB = constant.Constant( 'GL_ARRAY_BUFFER_BINDING_ARB', 0x8894 )
glget.addGLGetConstant( GL_ARRAY_BUFFER_BINDING_ARB, (1,) )
GL_ELEMENT_ARRAY_BUFFER_BINDING_ARB = constant.Constant( 'GL_ELEMENT_ARRAY_BUFFER_BINDING_ARB', 0x8895 )
glget.addGLGetConstant( GL_ELEMENT_ARRAY_BUFFER_BINDING_ARB, (1,) )
GL_VERTEX_ARRAY_BUFFER_BINDING_ARB = constant.Constant( 'GL_VERTEX_ARRAY_BUFFER_BINDING_ARB', 0x8896 )
glget.addGLGetConstant( GL_VERTEX_ARRAY_BUFFER_BINDING_ARB, (1,) )
GL_NORMAL_ARRAY_BUFFER_BINDING_ARB = constant.Constant( 'GL_NORMAL_ARRAY_BUFFER_BINDING_ARB', 0x8897 )
glget.addGLGetConstant( GL_NORMAL_ARRAY_BUFFER_BINDING_ARB, (1,) )
GL_COLOR_ARRAY_BUFFER_BINDING_ARB = constant.Constant( 'GL_COLOR_ARRAY_BUFFER_BINDING_ARB', 0x8898 )
glget.addGLGetConstant( GL_COLOR_ARRAY_BUFFER_BINDING_ARB, (1,) )
GL_INDEX_ARRAY_BUFFER_BINDING_ARB = constant.Constant( 'GL_INDEX_ARRAY_BUFFER_BINDING_ARB', 0x8899 )
glget.addGLGetConstant( GL_INDEX_ARRAY_BUFFER_BINDING_ARB, (1,) )
GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING_ARB = constant.Constant( 'GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING_ARB', 0x889A )
glget.addGLGetConstant( GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING_ARB, (1,) )
GL_EDGE_FLAG_ARRAY_BUFFER_BINDING_ARB = constant.Constant( 'GL_EDGE_FLAG_ARRAY_BUFFER_BINDING_ARB', 0x889B )
glget.addGLGetConstant( GL_EDGE_FLAG_ARRAY_BUFFER_BINDING_ARB, (1,) )
GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING_ARB = constant.Constant( 'GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING_ARB', 0x889C )
glget.addGLGetConstant( GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING_ARB, (1,) )
GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING_ARB = constant.Constant( 'GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING_ARB', 0x889D )
glget.addGLGetConstant( GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING_ARB, (1,) )
GL_WEIGHT_ARRAY_BUFFER_BINDING_ARB = constant.Constant( 'GL_WEIGHT_ARRAY_BUFFER_BINDING_ARB', 0x889E )
glget.addGLGetConstant( GL_WEIGHT_ARRAY_BUFFER_BINDING_ARB, (1,) )
GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING_ARB = constant.Constant( 'GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING_ARB', 0x889F )
GL_READ_ONLY_ARB = constant.Constant( 'GL_READ_ONLY_ARB', 0x88B8 )
GL_WRITE_ONLY_ARB = constant.Constant( 'GL_WRITE_ONLY_ARB', 0x88B9 )
GL_READ_WRITE_ARB = constant.Constant( 'GL_READ_WRITE_ARB', 0x88BA )
GL_BUFFER_ACCESS_ARB = constant.Constant( 'GL_BUFFER_ACCESS_ARB', 0x88BB )
GL_BUFFER_MAPPED_ARB = constant.Constant( 'GL_BUFFER_MAPPED_ARB', 0x88BC )
GL_BUFFER_MAP_POINTER_ARB = constant.Constant( 'GL_BUFFER_MAP_POINTER_ARB', 0x88BD )
GL_STREAM_DRAW_ARB = constant.Constant( 'GL_STREAM_DRAW_ARB', 0x88E0 )
GL_STREAM_READ_ARB = constant.Constant( 'GL_STREAM_READ_ARB', 0x88E1 )
GL_STREAM_COPY_ARB = constant.Constant( 'GL_STREAM_COPY_ARB', 0x88E2 )
GL_STATIC_DRAW_ARB = constant.Constant( 'GL_STATIC_DRAW_ARB', 0x88E4 )
GL_STATIC_READ_ARB = constant.Constant( 'GL_STATIC_READ_ARB', 0x88E5 )
GL_STATIC_COPY_ARB = constant.Constant( 'GL_STATIC_COPY_ARB', 0x88E6 )
GL_DYNAMIC_DRAW_ARB = constant.Constant( 'GL_DYNAMIC_DRAW_ARB', 0x88E8 )
GL_DYNAMIC_READ_ARB = constant.Constant( 'GL_DYNAMIC_READ_ARB', 0x88E9 )
GL_DYNAMIC_COPY_ARB = constant.Constant( 'GL_DYNAMIC_COPY_ARB', 0x88EA )
glBindBufferARB = platform.createExtensionFunction( 
'glBindBufferARB',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLuint,),
doc='glBindBufferARB(GLenum(target), GLuint(buffer)) -> None',
argNames=('target','buffer',),
deprecated=_DEPRECATED,
)

glDeleteBuffersARB = platform.createExtensionFunction( 
'glDeleteBuffersARB',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLsizei,arrays.GLuintArray,),
doc='glDeleteBuffersARB(GLsizei(n), GLuintArray(buffers)) -> None',
argNames=('n','buffers',),
deprecated=_DEPRECATED,
)

glGenBuffersARB = platform.createExtensionFunction( 
'glGenBuffersARB',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLsizei,arrays.GLuintArray,),
doc='glGenBuffersARB(GLsizei(n), GLuintArray(buffers)) -> None',
argNames=('n','buffers',),
deprecated=_DEPRECATED,
)

glIsBufferARB = platform.createExtensionFunction( 
'glIsBufferARB',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=constants.GLboolean, 
argTypes=(constants.GLuint,),
doc='glIsBufferARB(GLuint(buffer)) -> constants.GLboolean',
argNames=('buffer',),
deprecated=_DEPRECATED,
)

glBufferDataARB = platform.createExtensionFunction( 
'glBufferDataARB',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLsizeiptrARB,ctypes.c_void_p,constants.GLenum,),
doc='glBufferDataARB(GLenum(target), GLsizeiptrARB(size), c_void_p(data), GLenum(usage)) -> None',
argNames=('target','size','data','usage',),
deprecated=_DEPRECATED,
)

glBufferSubDataARB = platform.createExtensionFunction( 
'glBufferSubDataARB',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLintptrARB,constants.GLsizeiptrARB,ctypes.c_void_p,),
doc='glBufferSubDataARB(GLenum(target), GLintptrARB(offset), GLsizeiptrARB(size), c_void_p(data)) -> None',
argNames=('target','offset','size','data',),
deprecated=_DEPRECATED,
)

glGetBufferSubDataARB = platform.createExtensionFunction( 
'glGetBufferSubDataARB',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLintptrARB,constants.GLsizeiptrARB,ctypes.c_void_p,),
doc='glGetBufferSubDataARB(GLenum(target), GLintptrARB(offset), GLsizeiptrARB(size), c_void_p(data)) -> None',
argNames=('target','offset','size','data',),
deprecated=_DEPRECATED,
)

glMapBufferARB = platform.createExtensionFunction( 
'glMapBufferARB',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=ctypes.c_void_p, 
argTypes=(constants.GLenum,constants.GLenum,),
doc='glMapBufferARB(GLenum(target), GLenum(access)) -> ctypes.c_void_p',
argNames=('target','access',),
deprecated=_DEPRECATED,
)

glUnmapBufferARB = platform.createExtensionFunction( 
'glUnmapBufferARB',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=constants.GLboolean, 
argTypes=(constants.GLenum,),
doc='glUnmapBufferARB(GLenum(target)) -> constants.GLboolean',
argNames=('target',),
deprecated=_DEPRECATED,
)

glGetBufferParameterivARB = platform.createExtensionFunction( 
'glGetBufferParameterivARB',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,arrays.GLintArray,),
doc='glGetBufferParameterivARB(GLenum(target), GLenum(pname), GLintArray(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)

glGetBufferPointervARB = platform.createExtensionFunction( 
'glGetBufferPointervARB',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,ctypes.POINTER(ctypes.c_void_p),),
doc='glGetBufferPointervARB(GLenum(target), GLenum(pname), POINTER(ctypes.c_void_p)(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)


def glInitVertexBufferObjectARB():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
