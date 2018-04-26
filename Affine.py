import glfw
from OpenGL.GL import *
import numpy as np
import defs as defs


def render(M,u):
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    #defs.draw_coordinate()
    
    # draw a line segments from (-.6,.1) to (.0,.1) with an affine transformation
    glColor3ub(255,255,255)
    glBegin(GL_LINE_STRIP)
    glVertex2fv(M @ np.array([-.6,.1]) + u)
    glVertex2fv(M @ np.array([-.15,.1]) + u)
    glVertex2fv(M @ np.array([.0,.1]) + u)
    glEnd()

    # draw a line segments from (-.6,.2) to (.6, .2) with an affine transformation
    glBegin(GL_LINE_STRIP)
    glVertex2fv(M @ np.array([-.6,.2]) + u)
    glVertex2fv(M @ np.array([.0,.2]) + u)
    glVertex2fv(M @ np.array([.6,.2]) + u)
    glEnd()

def main():
    # Initialize the library
    if not glfw.init():
        return

    window = glfw.create_window(640,640,"OHT",None,None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    
    glfw.swap_interval(10)

    count = 0

    while not glfw.window_should_close(window):
        glfw.poll_events()
        
        M = np.array([1,1])
        u = np.array([.1,.1])

        render(M,u)
        

        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
