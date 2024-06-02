import pygame
import numpy as np

from OpenGL.GL import *

from engine2.GLApp.Transformations.Transformations import identity_mat, translate
from engine2.GLApp.Utils.GraphicsData import GraphicsData
from engine2.GLApp.Utils.Uniform import Uniform


class BaseMovingMesh:
    def __init__(self, program_id, vertices, vertex_colors, draw_type):
        self.program_id = program_id
        self.vertices = vertices
        self.draw_type = draw_type
        self.vao_ref = glGenVertexArrays(1)
        glBindVertexArray(self.vao_ref)
        position_variable = GraphicsData("vec3", self.vertices)
        position_variable.create_variable(program_id, "position")
        color_variable = GraphicsData("vec3", vertex_colors)
        color_variable.create_variable(program_id, "vertexColor")

    def draw(
            self,
            transformation_matrix
    ):
        transformation = Uniform("mat4", transformation_matrix)
        transformation.find_variable(self.program_id, "modelMatrix")
        transformation.load()
        glBindVertexArray(self.vao_ref)
        glDrawArrays(self.draw_type, 0, len(self.vertices))
