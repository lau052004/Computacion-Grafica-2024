import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Utils import *

pygame.init()

screen_width = 1000
screen_height = 800
ortho_width = 640
ortho_height = 480

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Graphs in PyOpenGL')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, ortho_width, 0, ortho_height)


def plot_point():
    glBegin(GL_POINTS)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()


def plot_lines():
    for l in points:
        glBegin(GL_LINE_STRIP)
        for coords in l:
            glVertex2f(coords[0], coords[1])
        glEnd()


done = False
init_ortho()
glPointSize(5)
# points: Una lista que almacenará todas las líneas dibujadas; cada línea es una lista de puntos.
points = []
# line: Una lista temporal para almacenar los puntos de la línea actualmente siendo dibujada.
line = []
# mouse_down: Una bandera para rastrear si el botón del ratón está presionado.
mouse_down = False

while not done:
    # p se inicializa como None en cada iteración, destinado a almacenar la posición del ratón si es relevante.
    p = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # Si el usuario presiona el botón del ratón, se comienza una nueva línea. line se reinicia y se agrega a points.
        elif event.type == MOUSEBUTTONDOWN:
            mouse_down = True
            line = []
            points.append(line)
        # Si el usuario suelta el botón del ratón, se finaliza el dibujo de la línea actual.
        elif event.type == MOUSEBUTTONUP:
            mouse_down = False
        # Si el ratón se mueve mientras el botón está presionado, se obtiene la posición del ratón y se agrega a la
        # línea actual. map_value (una función no definida en el fragmento de código proporcionado,
        # pero presumiblemente mapea un rango de valores a otro) ajusta las coordenadas del ratón al espacio de
        # coordenadas definido por la proyección ortogonal.
        elif event.type == MOUSEMOTION and mouse_down:
            p = pygame.mouse.get_pos()
            # Utils
            line.append((map_value(0, screen_width, 0, ortho_width, p[0]),
                         map_value(0, screen_height, ortho_height, 0, p[1])))

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plot_lines()
    pygame.display.flip()
    # pygame.time.wait(100)
pygame.quit()
