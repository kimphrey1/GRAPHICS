import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective

# the imports from Pygame and OpenGL are essential for creating a 3D graphical 
# application. Pygame handles window creation and input events, while OpenGL 
# provides the necessary functions for rendering graphics in a 3D space, 
# including perspective projection. The gluPerspective function is particularly 
# important for setting up the projection matrix in OpenGL.


pygame.init()
# "Initialize the Pygame library, allowing us to use its functionality 
# for creating graphical applications, handling events, and managing 
# multimedia elements in a Python program."

display = (800, 600)
# "Create a variable named 'display' that represents the dimensions of the 
# display or window. The width is 800 pixels, and the height is 600 pixels."


pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
# "Create a Pygame display window with the dimensions specified in the 'display' 
# variable (800 pixels wide, 600 pixels tall), and enable the use of double buffering 
# and OpenGL rendering."


gluPerspective(45, (display[0] / display[1]), 0.1, 100.0)  
# "Set up a perspective projection with a 45-degree field of view, aspect ratio determined 
# by the window's width and height, a near clipping plane at 0.1 units, and a far clipping 
# plane at 100.0 units."
# This line sets up a 3D perspective projection with a 45-degree field of view, adjusting 
# for the window's aspect ratio, and specifying near and far clipping planes.

glTranslatef(0.0, 0.0, -10)  

# translates (moves) the coordinate system along the z-axis by -10 units. In simple terms:
# "Move the drawing or objects in the scene 10 units backward along the z-axis."

# This command adjusts the initial position of the camera by moving it 10 units backward 
# along the z-axis, allowing for a suitable view of the 3D scene.


def draw_triangle():
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)  # red
    glVertex3f(0.0, 2.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)  # green
    glVertex3f(-2.0, -2.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)  # blue
    glVertex3f(2.0, -2.0, 0.0)
    glEnd()

# The glBegin(GL_TRIANGLES) command in OpenGL marks the beginning of a sequence of vertices that 
# define triangles. It indicates that the following vertices specified with glVertex3f will be used
# to create individual triangles until glEnd() is called.
# The function draw_triangle() uses OpenGL commands to draw a colored triangle in 3D space 
# with vertices at (0.0, 2.0, 0.0), (-2.0, -2.0, 0.0), and (2.0, -2.0, 0.0), colored red, green, 
# and blue, respectively.
# The glEnd() command in OpenGL marks the end of a sequence of vertices that define a geometric 
# primitive, such as triangles when used with glBegin(GL_TRIANGLES). It signifies the completion 
# of the vertex data for the specified primitive, and OpenGL processes the data to render the 
# corresponding shapes in the scene.

def translate(x, y, z):
    glTranslatef(x, y, z)

# The translate function takes three parameters (x, y, and z) and uses OpenGL's 
# glTranslatef to apply a translation to the current modelview matrix, effectively 
# moving the objects in the scene by the specified amounts along the x, y, and z axes.

# The glTranslatef(x, y, z) function in OpenGL is used to apply a translation to the current 
# modelview matrix, shifting the position of subsequent objects in the scene by specified 
# amounts along the x, y, and z axes.


def rotate(angle, x, y, z):
    glRotatef(angle, x, y, z)

# The rotate function takes an angle and three axis components (x, y, and z), using OpenGL's 
# glRotatef to apply a rotation to the current modelview matrix, resulting in a transformation 
# that rotates subsequent objects in the scene around the specified axis by the given angle.


def scale(sx, sy, sz):
    glScalef(sx, sy, sz)
# The scale function, utilizing OpenGL's glScalef, adjusts the current modelview matrix by scaling
# subsequent objects in the scene along the x, y, and z axes by the specified scaling 
# factors (sx, sy, and sz).


def display_triangle(frame_counter):
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
# The display_triangle function, given a frame_counter as a parameter, utilizes OpenGL commands
# (glClear) to clear the color and depth buffers, preparing for the rendering of a new frame in 
# a 3D scene.
# The frame_counter parameter in the display_triangle function tracks the number of frames 
# rendered, allowing dynamic adjustments to the display based on the current frame count within 
# the 3D scene.
    
    draw_triangle()
# The draw_triangle() function contains OpenGL commands to render a colored triangle in a 3D scene, 
# specifying vertices and their respective colors.

    # Transformations

# Uncomment one of the following sections to see the effect of the transformation

# __________________________________________________________________________________________
    # SECTION 1 (Translation)  
    if frame_counter < 300:
         translate(0.005, 0.005, 0.0)

# EXPLANATION
# "If the frame counter is less than 300, move (translate) the object slightly to the right 
# (positive x-direction) and slightly upwards (positive y-direction) by a small amount."
# The "frame counter" typically refers to a variable that counts the number of frames rendered 
# or displayed in a graphical application. In the context of computer graphics or animation, a 
# frame is a single image displayed on the screen. Frame counters are often used in animation 
# loops to keep track of the progression of time or frames.
#  It is used to control various aspects of the animation, such as determining when to apply 
# certain transformations or changes in the displayed content based on the elapsed frame count.
# __________________________________________________________________________________________



# __________________________________________________________________________________________
    # SECTION 2 (Rotation)  
    # rotate(5.0, 0.0, 0.0, 1.0)
         
# EXPLANATION
# "Rotate the object by 5 degrees around the axis that points in the positive direction of 
# the z-axis (the vertical axis)."

# In this case:

# The first parameter (5.0) is the angle of rotation, specified in degrees.
# The next three parameters (0.0, 0.0, 1.0) represent the axis of rotation. Here, 
# it is specifying a rotation around the z-axis, as the vector (0.0, 0.0, 1.0) points 
# in the positive z-direction.


# __________________________________________________________________________________________



# __________________________________________________________________________________________
    # # SECTION 3 (Scaling) 
    # if frame_counter < 200:
    #      scale(0.995, 0.995, 1.0)
         
# EXPLANATION
# "If the frame counter is less than 200, gradually scale down the size of the object. 
# The scaling factor is 0.995 in the x and y directions, while there is no scaling in the 
# z direction."

# In simpler terms, during the initial frames of the animation, the object will slowly 
# become smaller in the horizontal (x) and vertical (y) directions, while maintaining its 
# original size in the depth (z) direction.
# __________________________________________________________________________________________



# __________________________________________________________________________________________
    # SECTION 4 (Rotation and Scaling)
    # if frame_counter < 250:
    #     rotate(1.0, 0.0, 0.0, 1.0)
    # elif frame_counter < 350:
    #     scale(0.995, 0.995, 1.0)
    # elif frame_counter < 400:
    #     pass
         
# EXPLANATION
# "If the frame counter is less than 250, rotate the object slightly around the x-axis 
# (tilting it forward)."
# "Else if the frame counter is less than 350, gradually scale down the size of the object 
# in the x and y directions while maintaining its original size in the z direction."
# "Else if the frame counter is less than 400, do nothing (no additional transformation)."
# In summary, during different frame ranges, the object undergoes a rotation, a scaling, or 
# no transformation, depending on the current frame count.
# __________________________________________________________________________________________



# __________________________________________________________________________________________
    # # SECTION 5 (Scaling and Rotation)
    # if frame_counter < 200:
    #      scale(0.995, 0.995, 1.0)
    # elif frame_counter < 250:
    #     pass
    # else:
    #      rotate(1.0, 0.0, 0.0, 1.0)
         
# EXPLANATION
# "If the frame counter is less than 200, gradually scale down the size of the object in the 
# x and y directions while maintaining its original size in the z direction."
# "Else if the frame counter is less than 250, do nothing (no additional transformation)."
# "Else (if the frame counter is 250 or greater), rotate the object slightly around the x-axis 
# (tilting it forward)."
# In summary, during different frame ranges, the object undergoes a scaling, no transformation, 
# or a rotation, depending on the current frame count.  
# __________________________________________________________________________________________

    
# END OF SECTIONS

    pygame.display.flip()
# The pygame.display.flip() command essentially shows the changes
# made in the frame by updating the display, allowing you to see the 
# rendered content on the screen in a Pygame application.


glEnable(GL_DEPTH_TEST)
# The glEnable(GL_DEPTH_TEST) command in OpenGL activates the depth 
# testing mechanism, which ensures that objects closer to the viewer are 
# rendered in front of objects farther away, contributing to realistic rendering of 3D scenes.



frame_counter = 0
# The variable frame_counter is initialized with a value of 0, and it is typically used to
# keep track of the number of frames rendered in a graphics or animation loop.




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    display_triangle(frame_counter)
    frame_counter += 1
    pygame.time.wait(10)  



# In this code, there's an ongoing loop that continually renders frames 
# for a Pygame application. It monitors for any events, such as the user 
# closing the window, and exits the loop if the close event occurs. Inside 
# the loop, the display_triangle function is called to render the 3D scene 
# based on the current frame count (frame_counter). After rendering, the frame 
# counter is incremented, and the loop waits for 10 milliseconds before proceeding 
# to the next iteration. This setup allows for continuous animation and interaction 
# within the Pygame window.