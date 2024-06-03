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


    # azul
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(120, 5)
    glVertex2f(95, 30)
    glVertex2f(120, 55)
    glVertex2f(145, 30)
    glEnd()

    #amarillo
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(45, -20)
    glVertex2f(95, 30)
    glVertex2f(45, 80)
    glEnd()

    #verde
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(-5, 30)
    glVertex2f(45, -20)
    glVertex2f(45, 80)
    glEnd()

    #morado
    glBegin(GL_TRIANGLES)
    glColor3f(0.5, 0.0, 0.5)
    glVertex2f(17, 6)
    glVertex2f(10, -25)
    glVertex2f(-22, -21)
    glEnd()

    # naranja
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.75, 0.0)
    glVertex2f(17, 52)
    glVertex2f(12, 85)
    glVertex2f(-22, 81)
    glEnd()

    # rosa
    glBegin(GL_QUADS)
    glColor3f(1.5, 0.0, 0.5)
    glVertex2f(107, 115.5)
    glVertex2f(107, 82.5)
    glVertex2f(74, 51.5)
    glVertex2f(74, 83.5)
    glEnd()

    # rojo
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(97, -36)
    glVertex2f(62, -69)
    glVertex2f(62, 0)
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



