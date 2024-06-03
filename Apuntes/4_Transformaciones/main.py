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

    glMatrixMode(GL_PROJECTION)
    gluPerspective(40, (display[0] / display[1]), 0.1, 100)
    glTranslatef(0.0, 0, -40)
    glRotatef(45, 1, 1, 1)


def draw_world_axes():
    glLineWidth(4)
    glBegin(GL_LINES)
    glColor(1, 0, 0)
    glVertex3d(-1000, 0, 0)
    glVertex3d(1000, 0, 0)
    glColor(0, 1, 0)
    glVertex3d(0, -1000, 0)
    glVertex3d(0, 1000, 0)
    glColor(0, 0, 1)
    glVertex3d(0, 0, -1000)
    glVertex3d(0, 0, 1000)
    glEnd()


main()
run = True
points_matrix = generate_sphere_points()
current_angle = 0
angle_delta = 4
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    draw_world_axes()
    glLineWidth(1)
    glTranslatef(4, 0, 0)
    glRotatef(current_angle, 0, 0, 1)
    plot_parametric_mesh(points_matrix)
    pygame.display.flip()
    pygame.time.wait(10)
    current_angle += angle_delta
    current_angle %= 360
pygame.quit()
quit()
