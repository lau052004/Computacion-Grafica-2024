import os

import pygame
import numpy as np
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
    glRotatef(-45, 1, 0, 1)


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

trajectory_points = []

main()
run = True
points_matrix = generate_sphere_points()
a = 10
current_t = 0
t_delta = 0.08

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    draw_world_axes()

    x_pos = (a * np.cos(current_t)) / (1 + np.sin(current_t)**2)
    y_pos = (a * np.cos(current_t) * np.sin(current_t)) / (1 + np.sin(current_t)**2)
    z_pos = 0

    trajectory_points.append((x_pos, y_pos, z_pos))

    glColor3f(1.0, 1.0, 1.0)
    glLineWidth(2)
    glBegin(GL_LINE_STRIP)
    for point in trajectory_points:
        glVertex3fv(point)
    glEnd()


    glTranslatef(x_pos, y_pos, z_pos)
    plot_parametric_mesh(points_matrix)
    pygame.display.flip()
    pygame.time.wait(10)


    current_t += t_delta
    if current_t > 2 * np.pi:
        current_t -= 2 * np.pi
        trajectory_points.clear()

pygame.quit()
quit()