'''OpenGL extension INGR.blend_func_separate

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_INGR_blend_func_separate'
_DEPRECATED = False

glBlendFuncSeparateINGR = platform.createExtensionFunction( 
'glBlendFuncSeparateINGR',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLenum,constants.GLenum,),
doc='glBlendFuncSeparateINGR(GLenum(sfactorRGB), GLenum(dfactorRGB), GLenum(sfactorAlpha), GLenum(dfactorAlpha)) -> None',
argNames=('sfactorRGB','dfactorRGB','sfactorAlpha','dfactorAlpha',),
deprecated=_DEPRECATED,
)


def glInitBlendFuncSeparateINGR():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
