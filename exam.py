import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective


pygame.init()

display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

gluPerspective(45, (display[0] / display[1]), 0.1, 100.0)  
glTranslatef(0.0, 0.0, -10)  

def draw_triangle():
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)  # red
    glVertex3f(0.0, 2.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)  # green
    glVertex3f(-2.0, -2.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)  # blue
    glVertex3f(2.0, -2.0, 0.0)
    glEnd()

def translate(x, y, z):
    glTranslatef(x, y, z)

def rotate(angle, x, y, z):
    glRotatef(angle, x, y, z)

def scale(sx, sy, sz):
    glScalef(sx, sy, sz)

def display_triangle(frame_counter):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    draw_triangle()


    # Transformations

# Uncomment one of the following sections to see the effect of the transformation

# __________________________________________________________________________________________
    # SECTION 1 (Translation)  
    if frame_counter < 300:
         translate(0.005, 0.005, 0.0)
# __________________________________________________________________________________________



# __________________________________________________________________________________________
    # SECTION 2 (Rotation)  
    # rotate(5.0, 0.0, 0.0, 1.0)
# __________________________________________________________________________________________



# __________________________________________________________________________________________
    # # SECTION 3 (Scaling) 
    # if frame_counter < 200:
    #      scale(0.995, 0.995, 1.0)
# __________________________________________________________________________________________



# __________________________________________________________________________________________
    # SECTION 4 (Rotation and Scaling)
    if frame_counter < 250:
        rotate(1.0, 0.0, 0.0, 1.0)
    elif frame_counter < 350:
        scale(0.995, 0.995, 1.0)
    elif frame_counter < 400:
        pass
# __________________________________________________________________________________________



# __________________________________________________________________________________________
    # # SECTION 5 (Scaling and Rotation)
    # if frame_counter < 200:
    #      scale(0.995, 0.995, 1.0)
    # elif frame_counter < 250:
    #     pass
    # else:
    #      rotate(1.0, 0.0, 0.0, 1.0)
# __________________________________________________________________________________________

    
# END OF SECTIONS

    pygame.display.flip()

glEnable(GL_DEPTH_TEST)

frame_counter = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    display_triangle(frame_counter)
    frame_counter += 1
    pygame.time.wait(10)  
