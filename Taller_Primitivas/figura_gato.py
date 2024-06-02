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
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0, 0)
    glVertex2f(100, 0)
    glVertex2f(100, 100)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.6, 0.1, 0.4)  # Rosado oscuro (rojo moderado, verde bajo, azul moderado)
    glVertex2f(100, 0)
    glVertex2f(120, 60)
    glVertex2f(220, 100)
    glVertex2f(200, 40)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(30, 30)
    glVertex2f(100, 100)
    glVertex2f(30, 200)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(30, 79.79)
    glVertex2f(30, 200)
    glVertex2f(-40, 140)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.8)
    glVertex2f(0, 174.29)
    glVertex2f(44, 212)
    glVertex2f(0, 249.72)
    glVertex2f(-44, 212)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.6, 0.0)  # Naranja (rojo máximo, verde moderado, azul mínimo)
    glVertex2f(44, 212)
    glVertex2f(44, 300)
    glVertex2f(0, 249.72)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.6, 0.1, 0.8)  # Rosado oscuro (rojo moderado, verde bajo, azul moderado)
    glVertex2f(-44, 212)
    glVertex2f(-44, 300)
    glVertex2f(0, 249.72)
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
