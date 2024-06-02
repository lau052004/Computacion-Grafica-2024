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


main()
run = True
points_matrix = generate_sphere_points()
step = 0
step_change = 0.02
outer_radius = 10
inner_radius = outer_radius / 2.618
trajectory_points = []


vertices = []
for i in range(5):
    outer_angle = 2 * np.pi * i / 5
    inner_angle = outer_angle + np.pi / 5
    vertices.append((outer_radius * np.cos(outer_angle), outer_radius * np.sin(outer_angle)))
    vertices.append((inner_radius * np.cos(inner_angle), inner_radius * np.sin(inner_angle)))
vertices.append(vertices[0])

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    draw_world_axes()


    segment = int(step) % len(vertices)
    next_segment = (segment + 1) % len(vertices)
    t = step - int(step)
    x_pos = (1 - t) * vertices[segment][0] + t * vertices[next_segment][0]
    y_pos = (1 - t) * vertices[segment][1] + t * vertices[next_segment][1]


    trajectory_points.append((x_pos, y_pos, 0))

    if len(trajectory_points) > 1:
        glBegin(GL_LINE_STRIP)
        glColor3f(1.0, 1.0, 1.0)
        for vtx in trajectory_points:
            glVertex3fv(vtx)
        glEnd()


    glTranslatef(x_pos, y_pos, 0)
    glLineWidth(1)
    plot_parametric_mesh(points_matrix)
    pygame.display.flip()
    pygame.time.wait(10)

    step += step_change
    if step >= len(vertices):
        step = 0
        trajectory_points.clear()

pygame.quit()
quit()