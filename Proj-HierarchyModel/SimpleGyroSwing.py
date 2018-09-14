# Lotte-World "Advanced Gyro Swing"
# Hanyang Univesity Computer Graphics
# Made by Oh Hyun Taek

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

gCamAng = 0.

# if positive, make coordinate "real-line" else negative, "dotted-line"
def draw_coordinates():
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

    glBegin(GL_LINES)
    glColor3ub(255,0,0)
    for i in range(0,100,2):
        glVertex3fv(np.array([-i*.01,0.,0.]))
        glVertex3fv(np.array([-i*.01-.01,0.,0.]))
    glColor3ub(0,255,0)
    for i in range(0,100,2):
        glVertex3fv(np.array([0.,-i*.01,0.]))
        glVertex3fv(np.array([0.,-i*.01-.01,0.]))
    glColor3ub(0,0,255)
    for i in range(0,100,2):
        glVertex3fv(np.array([0.,0.,-i*.01]))
        glVertex3fv(np.array([0.,0.,-i*.01-.01]))
    glEnd()

# Structure outside
def draw_Swing_Structure():
    glBegin(GL_POLYGON)
    glColor3ub(255,128,0)
    glVertex3fv(np.array([0.05,0.4,0.4]))
    glVertex3fv(np.array([0.05,0.4,-0.4]))
    glVertex3fv(np.array([-0.05,0.4,-0.4]))
    glVertex3fv(np.array([-0.05,0.4,0.4]))
    glEnd()

    glBegin(GL_LINES)
    glColor3ub(255,128,0)
    glVertex3fv(np.array([0.05,0.4,0.4]))
    glVertex3fv(np.array([0.95,-0.8,0.4]))
    glVertex3fv(np.array([0.05,0.4,-0.4]))
    glVertex3fv(np.array([0.95,-0.8,-0.4]))
    glVertex3fv(np.array([-0.05,0.4,-0.4]))
    glVertex3fv(np.array([-0.95,-0.8,-0.4]))
    glVertex3fv(np.array([-0.05,0.4,0.4]))
    glVertex3fv(np.array([-0.95,-0.8,0.4]))
    glEnd()

def draw_Swing_bottom():
    glBegin(GL_POLYGON)
    glColor3ub(255,255,51)
    for th in np.linspace(0, 2*np.pi, 12+1)[:-1]:
        x = np.cos(th)*0.4
        y = -0.7
        z = np.sin(th)*0.4
        glVertex3fv([x,y,z])
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3ub(0,0,0)
    for th in np.linspace(0, 2*np.pi, 12+1)[:-1]:
        x = np.cos(th)*0.28
        y = -0.69998
        z = np.sin(th)*0.28
        glVertex3fv([x,y,z])
    glEnd()
    
    glBegin(GL_LINES)
    glColor3ub(255,255,255)
    for th in np.linspace(0, 2*np.pi, 12+1)[:-1]:
        x = np.cos(th)*0.28
        y = -0.699
        z = np.sin(th)*0.28
        glVertex3fv([0,y,0])
        glVertex3fv([x,y,z])
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex3fv(np.array([0.29,-0.698,0.29]))
    glVertex3fv(np.array([0.35,-0.698,0.29]))
    glVertex3fv(np.array([0.35,-0.698,0.35]))
    glVertex3fv(np.array([0.29,-0.698,0.35]))
    glEnd() 
    

def draw_Swing_pillar():
    glBegin(GL_QUADS)
    glColor3ub(153,102,0)
    glVertex3f( 0.1, 0.1,-0.1)
    glVertex3f(-0.1, 0.1,-0.1)
    glVertex3f(-0.1, 0.1, 0.1)
    glVertex3f( 0.1, 0.1, 0.1)
    glVertex3f( 0.1,-.72, 0.1)
    glVertex3f(-0.1,-.72, 0.1)
    glVertex3f(-0.1,-.72,-0.1)
    glVertex3f( 0.1,-.72,-0.1)

    glVertex3f( 0.1, 0.1,0.1)
    glVertex3f(-0.1, 0.1,0.1)
    glVertex3f(-0.1,-.72,0.1)
    glVertex3f( 0.1,-.72,0.1)
    glVertex3f( 0.1,-.72,-0.1)
    glVertex3f(-0.1,-.72,-0.1)
    glVertex3f(-0.1, 0.1,-0.1)
    glVertex3f( 0.1, 0.1,-0.1)
    
    glVertex3f(-0.1, 0.1, 0.1)
    glVertex3f(-0.1, 0.1,-0.1)
    glVertex3f(-0.1,-.72,-0.1)
    glVertex3f(-0.1,-.72, 0.1)
    glVertex3f(0.1,0.1,-0.1)
    glVertex3f(0.1,0.1,0.1)
    glVertex3f(0.1,-.72,0.1)
    glVertex3f(0.1,-.72,-0.1)
    glEnd()

def render(camAng,count,count2):
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glLoadIdentity()
    glOrtho(-1,1, -1,1, -10,10)

    # rotate "camera" position (right-multiply the current matrix by viewing matrix)
    # try to change parameters
    gluLookAt(1*np.sin(camAng),1,1*np.cos(camAng),0,0,0, 0,1,0)
    
    draw_coordinates()
    draw_Swing_Structure()

    glPushMatrix()
    glRotatef(count,0,0,1)
    draw_Swing_pillar()
    
    if count > 0 :
        dropFlag = count
    else :
        dropFlag = -count

    glPushMatrix()
    glTranslate(0,dropFlag*0.01-0.15,0)

    glPushMatrix()
    glRotatef(count2%360,0,1,0)
    draw_Swing_bottom()
    glPopMatrix()

    glPopMatrix()
    glPopMatrix()

def key_callback(window, key, scancode, action,mods):
    global gCamAng
    # rotate the camera when 1 or 3 key is pressed or repeated
    if action==glfw.PRESS or action==glfw.REPEAT:
        if key==glfw.KEY_1:
            gCamAng += np.radians(-10)
        elif key==glfw.KEY_3:
            gCamAng += np.radians(10)

def main():
    global gCamAng
    if not glfw.init():
        return
    window = glfw.create_window(640,640,'Advanced Gyro Swing',None,None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)
    count = 0
    count2 = 0
    Flag = True
    while not glfw.window_should_close(window):
        glfw.poll_events()
        render(gCamAng,count,count2)
        glfw.swap_buffers(window)
        count2 += 3
        if Flag == True :
            count += 1.5
        else :
            count -= 1.5

        if count > 100:
            Flag = False
        if count < -100 :
            Flag = True
    glfw.terminate()



if __name__ == "__main__":
    main()
