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

def drawTriangle():
    glBegin(GL_TRIANGLES)
    glVertex3fv(np.array([.0,.5,0.]))
    glVertex3fv(np.array([.0,.0,0.]))
    glVertex3fv(np.array([.5,.0,0.]))
    glEnd()

def drawTriangleTransformedBy(M):
    glBegin(GL_TRIANGLES)
    glVertex3fv( (M @ np.array([.0,.5,0.,1.]))[:-1])
    glVertex3fv( (M @ np.array([.0,.0,0.,1.]))[:-1])
    glVertex3fv( (M @ np.array([.5,.0,0.,1.]))[:-1])
    glEnd()

def render(camAng):
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)

    glLoadIdentity()
    
    # use orthogonal projection
    glOrtho(-1,1,-1,1,-1,1)

    # rotate "camera" position to see this 3D space better
    gluLookAt(-.1*np.sin(camAng),.1,.1*np.cos(camAng),0,0,0,0,1,0)
    
    defs.draw_coordinate()
    
    # rotate 30 deg about x axis
    th = np.radians(30)
    R = np.identity(4)
    R[:3,:3] = [[1.,0.,0.],
                [0.,np.cos(th),-np.sin(th)],
                [0.,np.sin(th),np.cos(th)]]

    # translate by (.4, 0., .2)
    T = np.identity(4)
    T[:3,3] = [.4,0.,.2]

    glColor3ub(255,255,255)
    #glRotatef(30,1,0,0)
    glMultMatrixf(R.T)
    #glMultMatrixf(T.T)
    
    drawTriangle()

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

    while not glfw.window_should_close(window):
        glfw.poll_events()
        
        render(gCamAng)

        glfw.swap_buffers(window)
    
    glfw.terminate()

if __name__ == "__main__":
    main()
