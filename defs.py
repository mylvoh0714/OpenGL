import glfw
from OpenGL.GL import *
import numpy as np

def draw_coordinate():
    #glClear(GL_COLOR_BUFFER_BIT)
    #glLoadIdentity()

    #draw coordinate
    glBegin(GL_LINES)
    glColor3ub(255,0,0)
    glVertex3fv(np.array([0.,0.,0.]))
    glVertex3fv(np.array([1.,0.,0.]))
    
    glColor3ub(0,255,0)
    glVertex3fv(np.array([0.,0.,0.]))
    glVertex3fv(np.array([0.,1.,0.]))

    glColor3ub(0,0,255)
    glVertex3fv(np.array([0.,0.,0]))
    glVertex3fv(np.array([0.,0.,1]))
    glEnd()

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
