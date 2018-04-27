import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import defs as defs

gCamAng = 0.

def render(camAng):
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glLoadIdentity()
    glOrtho(-1,1, -1,1, -10,10)

    # rotate "camera" position (right-multiply the current matrix by viewing matrix)
    # try to change parameters
    #gluLookAt(1*np.sin(camAng),1,1*np.cos(camAng),0,0,0, 0,1,0)
    para_eye = np.array([1*np.sin(camAng),-1,1*np.cos(camAng)])
    para_at = np.array([0.,0.,0.])
    para_up = np.array([0.,1.,0.])

    #myLookAt(para_eye,para_at,para_up)
    gluLookAt(1*np.sin(camAng),1,1*np.cos(camAng),0,0,0,0,1,0)

    defs.draw_coordinate()

    glPushMatrix()
    glScalef(.2,.2,.2)
    defs.drawBox() 

    glPushMatrix()
    glTranslate(0,0,.5)
    glColor3ub(0,255,0)
    defs.drawBox()
    glPopMatrix()

    glPopMatrix()
    

def myLookAt(eye,at,up): # eye,at,up are 1D numpy array of length 3
    w = eye-at
    w = w/np.sqrt(np.dot(w,w))

    u = np.cross(up,w)
    u = u/np.sqrt(np.dot(u,u))

    v = np.cross(w,u)

    M = np.identity(4)
    M[:3,:3] =  [[u[0],v[0],w[0]],
                [u[1],v[1],w[1]],
                [u[2],v[2],w[2]]]
    M[:3,3] = eye
    M = np.linalg.inv(M)
    glMultMatrixf(M.T)
   


def key_callback(window, key, scancode, action,mods):
    global gCamAng
    # rotate the camera when 1 or 3 key is pressed or repeated
    if action==glfw.PRESS or action==glfw.REPEAT:
        if key==glfw.KEY_1:
            gCamAng += np.radians(-10)
        elif key==glfw.KEY_3:
            gCamAng += np.radians(10)

def main():
    if not glfw.init():
        return
    window = glfw.create_window(640,640,'Lecture8',None,None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)
    while not glfw.window_should_close(window):
        glfw.poll_events()
        render(gCamAng)
        glfw.swap_buffers(window)
    
    glfw.terminate()



if __name__ == "__main__":
    main()
