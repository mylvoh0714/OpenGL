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

def render(camAng,count):
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)

    glLoadIdentity()
    
    # use orthogonal projection
    glOrtho(-1,1,-1,1,-1,1)
    # rotate "camera" position to see this 3D space better
    gluLookAt(.1*np.sin(camAng),.1,.1*np.cos(camAng),0,0,0,0,1,0)
    
    # draw the global frame
    defs.drawFrame()
    
    # blue base transformation
    glPushMatrix()
    glTranslatef(-.5+(count%360)*.003,0,0)

    # blue base drawing
    glPushMatrix()
    glScalef(.2,.2,.2)
    glColor3ub(0,0,255)
    defs.drawBox()
    glPopMatrix()

    # red arm transformation
    glPushMatrix()
    glRotatef(count%360,0,0,1)
    glTranslatef(.5,0,.01)

    # red arm drawing
    glPushMatrix()
    glScalef(.5,.1,.1)
    glColor3ub(255,0,0)
    defs.drawBox()
    glPopMatrix()

    glPopMatrix()
    glPopMatrix()

def main():
    
    global gCamAng
    if not glfw.init():
        return

    window = glfw.create_window(640,640,"OHT",None,None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glfw.set_key_callback(window,key_callback)
    glfw.swap_interval(1)

    count = 0
    while not glfw.window_should_close(window):
        glfw.poll_events()
        render(gCamAng,count) 
        count += 1

        glfw.swap_buffers(window)
    glfw.terminate()

if __name__ == "__main__":
    main()
