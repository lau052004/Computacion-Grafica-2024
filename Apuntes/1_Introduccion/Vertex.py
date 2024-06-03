import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

# Configuración de Dimensiones de la Ventana
screen_width = 1000
screen_height = 800

# Creación de la Ventana
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("OpenGL in Python")


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # gluOrtho2D(0, 640, 0, 480): Establece una proyección ortogonal 2D con los límites especificados,
    # lo que significa que se dibujará en un espacio de coordenadas donde el eje x va de 0 a 640 y el eje y de 0 a 480.
    gluOrtho2D(0, 640, 0, 480)


done = False
init_ortho()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Limpia los buffers de color y profundidad para preparar para el nuevo dibujo.
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    # Establece el tamaño de los puntos que serán dibujados.
    glPointSize(30)

    # Dibujo de Puntos
    glBegin(GL_POINTS)
    glVertex2i(100, 50)
    glVertex2i(630, 450)
    glEnd()

    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()
