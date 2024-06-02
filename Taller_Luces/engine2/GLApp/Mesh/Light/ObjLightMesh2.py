import random
from OpenGL.GL import *

from engine2.GLApp.Mesh.Light.BaseLightMesh import BaseLightMesh
from engine2.GLApp.Mesh.Moving.BaseMovingMesh import BaseMovingMesh


class ObjLightMesh2(BaseLightMesh):
    def __init__(self, program_id, filename):
        vertices, vertex_uvs, vertex_normals, faces = load_mesh(filename)
        colors = []
        for i in range(len(vertices)):
            colors.append([1, 1, 1])
        draw_type_aux = GL_TRIANGLES if len(faces[0]) == 3 else GL_QUADS
        super().__init__(program_id, vertices, vertex_uvs, vertex_normals, colors, draw_type_aux)
