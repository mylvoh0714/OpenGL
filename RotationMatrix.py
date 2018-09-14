import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
from OpenGL.arrays import vbo
import ctypes

gCamAng = 0.
gCamHeight = 1.

def drawUnitCube_glVertex():
    glBegin(GL_TRIANGLES)

    glNormal3f(0,1,0) # v0, v1, ... v5 normal
    glVertex3f( 0.5, 0.5,-0.5) # v0 position 
    glVertex3f(-0.5, 0.5,-0.5) # v1 position
    glVertex3f(-0.5, 0.5, 0.5) # v2 position
    
    glVertex3f( 0.5, 0.5,-0.5) # v3 position
    glVertex3f(-0.5, 0.5, 0.5) # v4 position
    glVertex3f( 0.5, 0.5, 0.5) # v5 position

    glNormal3f(0,-1,0) # v6, v7, ... v11 normal
    glVertex3f( 0.5,-0.5, 0.5) # v6 position
    glVertex3f(-0.5,-0.5, 0.5) # v7 position
    glVertex3f(-0.5,-0.5,-0.5) # v8 position

    glVertex3f( 0.5,-0.5, 0.5) # v9 position
    glVertex3f(-0.5,-0.5,-0.5) # v10 position
    glVertex3f( 0.5,-0.5,-0.5) # v11 position

    glNormal3f(0,0,1)
    glVertex3f( 0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5,-0.5, 0.5)

    glVertex3f( 0.5, 0.5, 0.5)
    glVertex3f(-0.5,-0.5, 0.5)
    glVertex3f( 0.5,-0.5, 0.5)

    glNormal3f(0,0,-1)
    glVertex3f( 0.5,-0.5,-0.5)
    glVertex3f(-0.5,-0.5,-0.5)
    glVertex3f(-0.5, 0.5,-0.5)

    glVertex3f( 0.5,-0.5,-0.5)
    glVertex3f(-0.5, 0.5,-0.5)
    gVertexArrayIndexed, gIndexArray = createVertexAndIndexArrayIndexed()
    glVertex3f( 0.5, 0.5,-0.5)

    glNormal3f(-1,0,0)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5,-0.5)
    glVertex3f(-0.5,-0.5,-0.5)

    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5,-0.5,-0.5)
    glVertex3f(-0.5,-0.5, 0.5)

    glNormal3f(1,0,0)
    glVertex3f( 0.5, 0.5,-0.5)
    glVertex3f( 0.5, 0.5, 0.5)
    glVertex3f( 0.5,-0.5, 0.5)

    glVertex3f( 0.5, 0.5,-0.5)
    glVertex3f( 0.5,-0.5, 0.5)
    glVertex3f( 0.5,-0.5,-0.5)
    glEnd()

def createVertexArraySeparate():
    varr = np.array([
            [0,1,0],         # v0 normal
            [0.5,0.5,-0.5],  # v0 position
            [0,1,0],         # v1 normal
            [-0.5,0.5,-0.5], # v1 position
            [0,1,0],         # v2 normal
            [-0.5,0.5,0.5],  # v2 position

            [0,1,0],         # v3 normal
            [0.5,0.5,-0.5],  # v3 position
            [0,1,0],         # v4 normal
            [-0.5,0.5,0.5],  # v4 position
            [0,1,0],         # v5 normal
            [0.5,0.5,0.5],   # v5 position

            [0,-1,0],        # v6 normal
            [0.5,-0.5,0.5],  # v6 position
            [0,-1,0],        # v7 normal
            [-0.5,-0.5,0.5], # v7 position
            [0,-1,0],        # v8 normal
            [-0.5,-0.5,-0.5],# v8 position

            [0,-1,0],
            [ 0.5,-0.5, 0.5],
            [0,-1,0],
            [-0.5,-0.5,-0.5],
            [0,-1,0],
            [ 0.5,-0.5,-0.5],

            [0,0,1],
            [ 0.5, 0.5, 0.5],
            [0,0,1],
            [-0.5, 0.5, 0.5],
            [0,0,1],
            [-0.5,-0.5, 0.5],

            [0,0,1],
            [ 0.5, 0.5, 0.5],
            [0,0,1],
            [-0.5,-0.5, 0.5],
            [0,0,1],
            [ 0.5,-0.5, 0.5],
            
            [0,0,-1],
            [ 0.5,-0.5,-0.5],
            [0,0,-1],
            [-0.5,-0.5,-0.5],
            [0,0,-1],
            [-0.5, 0.5,-0.5],

            [0,0,-1],
            [ 0.5,-0.5,-0.5],
            [0,0,-1],
            [-0.5, 0.5,-0.5],
            [0,0,-1],
            [ 0.5, 0.5,-0.5],

            [-1,0,0],
            [-0.5, 0.5, 0.5],
            [-1,0,0],
            [-0.5, 0.5,-0.5],
            [-1,0,0],
            [-0.5,-0.5,-0.5],

            [-1,0,0],
            [-0.5, 0.5, 0.5],
            [-1,0,0],
            [-0.5,-0.5,-0.5],
            [-1,0,0],
            [-0.5,-0.5, 0.5],

            [1,0,0],
            [ 0.5, 0.5,-0.5],
            [1,0,0],
            [ 0.5, 0.5, 0.5],
            [1,0,0],
            [ 0.5,-0.5, 0.5],

            [1,0,0],
            [ 0.5, 0.5,-0.5],
            [1,0,0],
            [ 0.5,-0.5, 0.5],
            [1,0,0],
            [ 0.5,-0.5,-0.5],
            ], 'float32')
    return varr

#def createVertexAndIndexArrayIndexed():
#    varr = np.array([
#            normalized([1,1,-1]),
#            [0.5,0.5,-0.5],
#
#            normalized([-1,1,-1]),
#            [-0.5,0.5,-0.5],
#
#            normalized([-1,1,-1]),
#            [-0.5,0.5,0.5],
#
#            normalized([1,1,1]),
#            [0.5,0.5,0.5],
#
#            normalized([1,-1,1]),
#            [0.5,-0.5,0.5],
#
#            normalized([-1,-1,1]),
#            [-0.5,-0.5,0.5],
#
#            normalized([-1,-1,-1]),
#            [-0.5,-0.5,-0.5],
#
#            normalized([1,-1,-1]),
#            [0.5,-0.5,-0.5],
#            ], 'float32')
#    iarr = np.array([
#        [0,1,2],
#        [0,2,3],
#        [4,5,6],
#        [4,6,7],
#        [3,2,5],
#        [3,5,4],
#        [7,6,1],
#        [7,1,0],
#        [2,1,6],
#        [2,6,5],
#        [0,3,4],
#        [0,4,7],
#        ])
#    return varr, iarr
#
#
#def l2norm(v):
#    return np.sqrt(np.dot(v, v))
#
#def normalized(v):
#    l = l2norm(v)
#    return 1/l * np.array(v)

def drawUnitCube_glDrawElements():
    global gVertexArrayIndexed, gIndexArray
    varr = gVertexArrayIndexed
    iarr = gIndexArray
    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_NORMAL_ARRAY)
    glNormalPointer(GL_FLOAT, 6*varr.itemsize,varr)
    glVertexPointer(3, GL_FLOAT,6*varr.itemsize,
    ctypes.c_void_p(varr.ctypes.data + 3*varr.itemsize))
    glDrawElements(GL_TRIANGLES, iarr.size,GL_UNSIGNED_INT, iarr)


def drawUnitCube_glDrawArray():
    global gVertexArraySeparate
    varr = gVertexArraySeparate
    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_NORMAL_ARRAY)
    glNormalPointer(GL_FLOAT, 6*varr.itemsize, varr)
    glVertexPointer(3, GL_FLOAT, 6*varr.itemsize,
            ctypes.c_void_p(varr.ctypes.data + 3*varr.itemsize))
    glDrawArrays(GL_TRIANGLES, 0, int(varr.size/6))

def drawFrame():
    glBegin(GL_LINES)
    glColor3ub(255, 0, 0)
    glVertex3fv(np.array([0.,0.,0.]))
    glVertex3fv(np.array([1.,0.,0.]))
    glColor3ub(0, 255, 0)
    glVertex3fv(np.array([0.,0.,0.]))
    glVertex3fv(np.array([0.,1.,0.]))
    glColor3ub(0, 0, 255)
    glVertex3fv(np.array([0.,0.,0]))
    glVertex3fv(np.array([0.,0.,1.]))
    glEnd()

def key_callback(window, key, scancode, action,mods):
    global gCamAng, gCamHeight
    if action==glfw.PRESS or action==glfw.REPEAT:
        if key==glfw.KEY_1:
            gCamAng += np.radians(-10)
        elif key==glfw.KEY_3:
            gCamAng += np.radians(10)
        elif key==glfw.KEY_2:
            gCamHeight += .1
        elif key==glfw.KEY_W:
            gCamHeight += -.1

gVertexArraySeparate = None

def render(ang):
    global gCamAng, gCamHeight
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1, 1,10)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(5*np.sin(gCamAng),gCamHeight,5*np.cos(gCamAng),0,0,0, 0,1,0)

    drawFrame() # draw global frame
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_RESCALE_NORMAL) # rescale normal

    glLightfv(GL_LIGHT0,GL_POSITION,(1.,2.,3.,1.))
    glLightfv(GL_LIGHT0,GL_AMBIENT,(.1,.1,.1,1.))
    glLightfv(GL_LIGHT0,GL_DIFFUSE,(1.,1.,1.,1.))
    glLightfv(GL_LIGHT0,GL_SPECULAR,(1.,1.,1.,1.))

    # ZYX Euler angles
    xang = np.radians(ang)
    yang = np.radians(30)
    zang = np.radians(30)
    M = np.identity(4)
    Rx = np.array([[1,0,0],
        [0, np.cos(xang), -np.sin(xang)],
        [0, np.sin(xang), np.cos(xang)]])
    Ry = np.array([[np.cos(yang), 0, np.sin(yang)],
        [0,1,0],
        [-np.sin(yang), 0, np.cos(yang)]])
    Rz = np.array([[np.cos(zang), -np.sin(zang), 0],
        [np.sin(zang), np.cos(zang), 0],
        [0,0,1]])
    
    R = Rz @ Ry @ Rx
    # # check inverse rotation
    #R = Rz @ Ry @ Rx.T

    # # check R @ R.T
    #print(R @ R.T)

    # # check determinant
    #print(np.linalg.det(R))

    M[:3,:3] = R
    glMultMatrixf(M.T)

    glScalef(.5,.5,.5)

    # draw cubes
    glMaterialfv(GL_FRONT,GL_AMBIENT_AND_DIFFUSE, (.5,.5,.5,1.))
    drawUnitCube_glDrawArray()
    
    glTranslatef(1.5,0,0)
    glMaterialfv(GL_FRONT,GL_AMBIENT_AND_DIFFUSE, (1.,0.,0.,1.))
    drawUnitCube_glDrawArray()
        
    glTranslatef(-1.5,1.5,0)
    glMaterialfv(GL_FRONT,GL_AMBIENT_AND_DIFFUSE, (0.,1.,0.,1.))
    drawUnitCube_glDrawArray()
    
    glTranslatef(0,-1.5,1.5)
    glMaterialfv(GL_FRONT,GL_AMBIENT_AND_DIFFUSE, (0.,0.,1.,1.))
    drawUnitCube_glDrawArray()
    glDisable(GL_LIGHTING)

def main():
    global gVertexArraySeparate

    if not glfw.init():
        return
    window = glfw.create_window(640,640,'2015058204',None,None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)
    glfw.swap_interval(1)

    gVertexArraySeparate = createVertexArraySeparate()

    count = 0
    while not glfw.window_should_close(window):
        glfw.poll_events()
        ang = count % 360
        render(ang)
        count += 1
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()












            
            

