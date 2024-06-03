import os

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

from MeshRenderer import plot_parametric_mesh, generate_sphere_points, generate_toroid_points

os.environ["SDL_VIDEO_CENTERED"] = '1'


def main():
    pygame.init()
    display = (1000, 1080)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0, -20)
    glRotatef(-90, 2, 0, 0)


main()
run = True
points_matrix = generate_toroid_points()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    glRotatef(4, 3, -10, -45)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    plot_parametric_mesh(points_matrix)
    pygame.display.flip()
    pygame.time.wait(10)
pygame.quit()
quit()
