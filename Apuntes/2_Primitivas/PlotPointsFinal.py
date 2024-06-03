import math
import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Este código crea una ventana utilizando Pygame y OpenGL para graficar la función cos(2πx) en el rango de x=0 a x=4
pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Graphs in PyOpenGL')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 4, -1, 1)

# La función plot_graph dibuja el gráfico punto por punto. Para cada valor de x en el rango de 0 a 4, calcula
# y=e(−x) cos(2πx) y coloca un punto en esas coordenadas.
def plot_graph():
    glBegin(GL_POINTS)
    px: GL_DOUBLE
    py: GL_DOUBLE
    # Se utiliza np.arange(0, 4, 0.005) para generar los valores de x con un paso de 0.005, proporcionando una buena
    # resolución para el gráfico.
    for px in np.arange(0, 4, 0.005):
        py = math.exp(-px) * math.cos(2 * math.pi * px)
        glVertex2f(px, py)
    glEnd()


done = False
init_ortho()
glPointSize(5)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plot_graph()
    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()
