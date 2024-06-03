import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
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


def dibujar_estrellas():

    for p in estrellas:
        glBegin(GL_LINE_STRIP)
        glColor3f(1, 1, 0)
        # arriba
        #puntos.append((p[0], p[1]))
        glVertex2f(p[0], p[1])

        # lados inferior derecho
        #puntos.append((p[0] + 12, p[1] - 32))
        glVertex2f(p[0] + 12, p[1] - 32)

        # lado del medio izquierdo
        glColor3f(1, 1, 0)
        #puntos.append((p[0] - 20, p[1] - 15))
        glVertex2f(p[0] - 20, p[1] - 15)

        # lado del medio derecho
        #puntos.append((p[0] + 20, p[1] - 15))
        glVertex2f(p[0] + 20, p[1] - 15)

        # lados inferior izquierdo
        glColor3f(1, 1, 0)
        #puntos.append((p[0] - 12, p[1] - 32))
        glVertex2f(p[0] - 12, p[1] - 32)

        # arriba
        #puntos.append((p[0], p[1]))
        glVertex2f(p[0], p[1])
        glEnd()
    #dibujar_lineas_puntos()



def dibujar_lineas_estrellas():
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(*estrellas[0])
    glVertex2f(*estrellas[1])
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(*estrellas[1])
    glVertex2f(*estrellas[2])
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(*estrellas[0])
    glVertex2f(*estrellas[3])
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(*estrellas[0])
    glVertex2f(*estrellas[4])
    glEnd()


def dibujar_lineas_puntos():
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 1.0)
    for i in range(len(puntos) - 1):
        glVertex2f(*puntos[i])
        glVertex2f(*puntos[i + 1])
    glEnd()
    puntos.clear()


done = False
init_ortho()
glPointSize(5)

puntos = []
estrellas = [(0, 0),
    (-40, 100),
    (-120, 300), (-15, -200),(300,-100)]

while not done:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()



    dibujar_estrellas()

    if len(estrellas) >= 2:
        dibujar_lineas_estrellas()

    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()
