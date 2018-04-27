import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import defs as defs

gCamAng = 0.

def key_callback(window,key,scancode,action,mods):
    global gCamAng
    if action == glfw.PRESS:
        if key == glfw.KEY_1:
            gCamAng += np.radians(-10)
        elif key == glfw.KEY_3:
            gCamAng += np.radians(10)


