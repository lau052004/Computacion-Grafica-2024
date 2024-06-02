import pygame
import numpy as np

from OpenGL.GL import *

from engine2.GLApp.Transformations.Transformations import identity_mat, translate
from engine2.GLApp.Utils.GraphicsData import GraphicsData
from engine2.GLApp.Utils.Uniform import Uniform


class BaseMeshU:
    def __init__(self, program_id, vertices, vertex_colors, draw_type, translation=[0, 0, 0]):
        self.vertices = vertices
        self.draw_type = draw_type
        self.vao_ref = glGenVertexArrays(1)
        glBindVertexArray(self.vao_ref)
        position_variable = GraphicsData("vec3", self.vertices)
        position_variable.create_variable(program_id, "position")
        color_variable = GraphicsData("vec3", vertex_colors)
        color_variable.create_variable(program_id, "vertexColor")
        self.transformation_matrix = identity_mat()
        self.transformation_matrix = translate(self.transformation_matrix, translation[0], translation[1], translation[2])
        self.transformation = Uniform("mat4", self.transformation_matrix)
        self.transformation.find_variable(program_id, "modelMatrix")

    def draw(self):
        self.transformation.load()
        glBindVertexArray(self.vao_ref)
        glDrawArrays(self.draw_type, 0, len(self.vertices))
