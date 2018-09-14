import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
from OpenGL.arrays import vbo
import ctypes

gCamAng = 0.
gCamHeight = 1.
gZoom = 3.

wireframe = False

def render(ang):
    global gCamAng, gCamHeight, gZoom
    global wireframe

    if wireframe == True :
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    else :
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION) # use projection matrix stack for projection transformation for correct lighting
    
    glLoadIdentity()
    glFrustum(-1,1,-1,1,gZoom,10)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    gluLookAt(5*np.sin(gCamAng),gCamHeight,5*np.cos(gCamAng), 0,0,0, 0,1,0)
    
    #drawFrame()

    glEnable(GL_LIGHTING) # try to uncomment: no lighting
    
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)
    glEnable(GL_LIGHT2)
    #glEnable(GL_LIGHT3)
    #glEnable(GL_LIGHT4)
    #glEnable(GL_LIGHT5)


    # light position
    glPushMatrix()
    
    #glRotatef(ang,0,1,0) # try to uncomment : rotate light

    lightPos0 = (1.,0.,0.,0.) # try to change 4th element to 0. or 1.
    lightPos1 = (1., .5, 0., 0.)
    lightPos2 = (1.,-.5,.5,0.)
    #lightPos3 = (0.,-1.,0.,0.)
    #lightPos4 = (0.,0.,1.,0.)
    #lightPos5 = (0.,0.,-1.,0.)
  
    glLightfv(GL_LIGHT0, GL_POSITION, lightPos0)
    glLightfv(GL_LIGHT1, GL_POSITION, lightPos1)  
    glLightfv(GL_LIGHT2, GL_POSITION, lightPos2)  
    #glLightfv(GL_LIGHT3, GL_POSITION, lightPos3)  
    #glLightfv(GL_LIGHT4, GL_POSITION, lightPos4)  
    #glLightfv(GL_LIGHT5, GL_POSITION, lightPos5)  
    glPopMatrix()

    # light intensity for each color channel
    ambientLightColor = (.1,.1,.1,1.)
    diffuseLightColor = (1.,1.,1.,1.)
    specularLightColor = (.2,.2,.2,.5)
    glLightfv(GL_LIGHT0, GL_AMBIENT,ambientLightColor)
    glLightfv(GL_LIGHT0, GL_DIFFUSE,diffuseLightColor)
    glLightfv(GL_LIGHT0, GL_SPECULAR,specularLightColor)
    
    glLightfv(GL_LIGHT1, GL_AMBIENT,ambientLightColor)
    glLightfv(GL_LIGHT1, GL_DIFFUSE,diffuseLightColor)
    glLightfv(GL_LIGHT1, GL_SPECULAR,specularLightColor)
    
    glLightfv(GL_LIGHT2, GL_AMBIENT,ambientLightColor)
    glLightfv(GL_LIGHT2, GL_DIFFUSE,diffuseLightColor)
    glLightfv(GL_LIGHT2, GL_SPECULAR,specularLightColor)

    #glLightfv(GL_LIGHT3, GL_AMBIENT,ambientLightColor)
    #glLightfv(GL_LIGHT3, GL_DIFFUSE,diffuseLightColor)
    #glLightfv(GL_LIGHT3, GL_SPECULAR,specularLightColor)

    #glLightfv(GL_LIGHT4, GL_AMBIENT,ambientLightColor)
    #glLightfv(GL_LIGHT4, GL_DIFFUSE,diffuseLightColor)
    #glLightfv(GL_LIGHT4, GL_SPECULAR,specularLightColor)
    
    #glLightfv(GL_LIGHT5, GL_AMBIENT,ambientLightColor)
    #glLightfv(GL_LIGHT5, GL_DIFFUSE,diffuseLightColor)
    #glLightfv(GL_LIGHT5, GL_SPECULAR,specularLightColor)
    
    #material reflectance for each color channel
    diffuseObjectColor = (1.,0.,0.,1.)
    specularObjectColor = (1.,0.,0.,1.)
    glMaterialfv(GL_FRONT,GL_AMBIENT_AND_DIFFUSE, diffuseObjectColor)
    glMaterialfv(GL_FRONT, GL_SPECULAR,specularObjectColor)
    
    glPushMatrix()
    #glRotatef(ang,0,1,0) # try to uncomment : rotate object
    
    glColor3ub(0, 0,255)

    drawUnitCube_glDrawArray()
    glPopMatrix()

    glDisable(GL_LIGHTING)

def drawUnitCube_glDrawArray():
    global gNormalandVertex_Arr
    varr = gNormalandVertex_Arr
    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_NORMAL_ARRAY)
    glNormalPointer(GL_FLOAT, 6*varr.itemsize, varr)
    glVertexPointer(3, GL_FLOAT, 6*varr.itemsize, ctypes.c_void_p(varr.ctypes.data + 3*varr.itemsize))
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


gNormalandVertex_Arr = np.array([],'float32')
def obj_parser(filename):
    global gNormalandVertex_Arr
    gNormalandVertex_Arr = np.array([],'float32')
    lines = open(filename,'r').read().split('\n')
    
    # number of vertex and normal
    v_cnt = 0
    vn_cnt = 0

    # number of faces
    Total_cnt=0
    tri_cnt=0
    quad_cnt=0
    poly_cnt=0

    for line in lines:
        if line[:2] == 'v ':
            v_cnt += 1
            line = line[2:].split()
            line = np.array(line,'float32')
            if v_cnt == 1 :
                vertexArr = np.array(line,'float32')
            else :
                vertexArr = np.vstack((vertexArr,line))
        
        elif line[:3] == 'vn ':
            vn_cnt += 1
            line = line[3:].split()
            line = np.array(line,'float32')
            if vn_cnt == 1 :
                normalArr = np.array(line,'float32')
            else :
                normalArr = np.vstack((normalArr,line))

        elif line[:2] == 'f ':
            Total_cnt += 1
            line = line.split()

            if len(line) == 4 :  # face with 3 vertices
                tri_cnt += 1
                line = line[1:]
                for i in range(len(line)):
                    line[i] = line[i].split('/')
                    nindex = int(line[i][2])-1
                    vindex = int(line[i][0])-1
                    if Total_cnt == 1 and i == 0 :
                        gNormalandVertex_Arr = np.array(normalArr[nindex],'float32')
                        gNormalandVertex_Arr = np.vstack((gNormalandVertex_Arr,vertexArr[vindex]))
                    else :
                        gNormalandVertex_Arr = np.vstack((gNormalandVertex_Arr,normalArr[nindex]))
                        gNormalandVertex_Arr = np.vstack((gNormalandVertex_Arr,vertexArr[vindex]))

            elif len(line) == 5 : # face with 4 vertices
                quad_cnt += 1
                line = line[1:] # line = [f0(v/n),f1(v/n),f2(v/n),f3(v/n)]
                for i in range(len(line)):
                    line[i] = line[i].split('/')
                
                for i in range(1,2):
                    nindex = int(line[0][2])-1
                    vindex = int(line[0][0])-1
                    if Total_cnt == 1 and i == 1 :
                        gNormalandVertex_Arr = np.array(normalArr[nindex],'float32')
                        gNormalandVertex_Arr = np.vstack((gNormalandVertex_Arr,vertexArr[vindex]))
                    else :
                        gNormalandVertex_Arr = np.vstack((gNormalandVertex_Arr,normalArr[nindex]))
                        gNormalandVertex_Arr = np.vstack((gNormalandVertex_Arr,vertexArr[vindex]))
                    
                    nindex = int(line[i][2])-1
                    vindex = int(line[i][0])-1
                    gNormalandVertex_Arr = np.vstack((gNormalandVertex_Arr,normalArr[nindex]))
                    gNormalandVertex_Arr = np.vstack((gNormalandVertex_Arr,vertexArr[vindex]))
                    
                    nindex = int(line[i+1][2])-1
                    vindex = int(line[i+1][0])-1
                    gNormalandVertex_Arr = np.vstack((gNormalandVertex_Arr,normalArr[nindex]))
                    gNormalandVertex_Arr = np.vstack((gNormalandVertex_Arr,vertexArr[vindex]))

            elif len(line) > 5 :
                poly_cnt += 1
                line = line[1:]
                for i in range(len(line)):
                    line[i] = line[i].split('/')

                for i in range(1,len(line)-2):
                    nindex = int(line[0][2])-1
                    vindex = int(line[0][0])-1
                    if Total_cnt == 1 and i == 1 :
                        gNormalandVertex_Arr = np.array(normalArr[nindex],'float32')
                        gNormalandVertex_Arr = np.vstack((gNormalandVertex_Arr,vertexArr[vindex]))
                    else :
                        gNormalandVertex_Arr = np.vstack((gNormalandVertex_Arr,normalArr[nindex]))
                        gNormalandVertex_Arr = np.vstack((gNormalandVertex_Arr,vertexArr[vindex]))
                    
                    nindex = int(line[i][2])-1
                    vindex = int(line[i][0])-1
                    gNormalandVertex_Arr = np.vstack((gNormalandVertex_Arr,normalArr[nindex]))
                    gNormalandVertex_Arr = np.vstack((gNormalandVertex_Arr,vertexArr[vindex]))
                    
                    nindex = int(line[i+1][2])-1
                    vindex = int(line[i+1][0])-1
                    gNormalandVertex_Arr = np.vstack((gNormalandVertex_Arr,normalArr[nindex]))
                    gNormalandVertex_Arr = np.vstack((gNormalandVertex_Arr,vertexArr[vindex]))
    
    print("File name : ", filename)
    print("Total Number of faces : ", Total_cnt)
    print("Number of faces with 3 vertices : ", tri_cnt)
    print("Number of faces with 4 vertices : ", quad_cnt)
    print("Number of faces with more than 4 vertices : ", poly_cnt)

#def dropp_callback():
#    
#    #filename = 'cylinder-tri.obj'
#    #filename = 'cylinder-tri-quad-n.obj'
#    
#    #filename = 'sphere-tri.obj'
#    #filename = 'sphere-tri-quad.obj'
#    #filename = 'CHALLENGER71.obj'
#    #filename = 'Wolf_One_obj.obj'
#    filename = 'hand.OBJ'
#    obj_parser(filename)


def drop_callback(window, filename):
    for i in filename:
        obj_parser(i)

def key_callback(window, key, scancode, action,mods):
    global gCamAng, gCamHeight, gZoom, wireframe
    if action==glfw.PRESS or action==glfw.REPEAT:
        if key==glfw.KEY_1:
            gCamAng += np.radians(-10)
        elif key==glfw.KEY_3:
            gCamAng += np.radians(10)
        elif key==glfw.KEY_2:
            gCamHeight += .1
        elif key==glfw.KEY_W:
            gCamHeight += -.1
        elif key==glfw.KEY_A:
            gZoom += .2
        elif key==glfw.KEY_S:
            gZoom -= .2
        elif key==glfw.KEY_Z:
            wireframe = not wireframe


def main():
    global gNormalandVertex_Arr

    if not glfw.init():
        return
    window = glfw.create_window(640,640,'2015058204',None,None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)
    glfw.set_drop_callback(window, drop_callback)
    #dropp_callback()
    glfw.swap_interval(1)

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












            
            

