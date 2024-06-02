import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

from Utils import *

pygame.init()

screen_width = 800
screen_height = 800
ortho_left = -400
ortho_right = 400
ortho_top = -400
ortho_bottom = 400

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Polygons in PyOpenGL')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(ortho_left, ortho_right, ortho_top, ortho_bottom)


def plot_polygon():
    # GL_TRIANGLES
    # GL_TRIANGLE_STRIP
    # GL_TRIANGLE_FAN
    # GL_QUADS
    # GL_QUAD_STRIP

    #azul
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(-60, 40)
    glVertex2f(-90, 70)
    glVertex2f(-60, 100)
    glVertex2f(-30, 70)
    glEnd()

    #naranja
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.75, 0.0)
    glVertex2f(-60, 40)
    glVertex2f(-120, 40)
    glVertex2f(-90, 70)
    glEnd()

    # verde
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0, 100)
    glVertex2f(60, 40)
    glVertex2f(-60, 40)
    glEnd()

    #amarillo
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(-20, 40)
    glVertex2f(60, 40)
    glVertex2f(60, -40)
    glEnd()

    #morado
    glBegin(GL_TRIANGLES)
    glColor3f(0.5, 0.0, 0.5)
    glVertex2f(60, -40)
    glVertex2f(90, -70)
    glVertex2f(30, -70)
    glEnd()

    #rojo
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(115, -15)
    glVertex2f(60, 40)
    glVertex2f(60, -15)
    glEnd()

    #rosa
    glBegin(GL_QUADS)
    glColor3f(1.5, 0.0, 0.5)
    glVertex2f(115, -15)
    glVertex2f(150, -50)
    glVertex2f(115, -50)
    glVertex2f(80, -15)
    glEnd()

done = False
init_ortho()

while not done:
    p = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plot_polygon()
    pygame.display.flip()
pygame.quit()



