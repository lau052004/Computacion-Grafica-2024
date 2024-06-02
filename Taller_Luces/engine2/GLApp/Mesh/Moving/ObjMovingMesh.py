import random
from OpenGL.GL import *

from engine2.GLApp.Mesh.Moving.BaseMovingMesh import BaseMovingMesh
from engine2.GLApp.Mesh.Uniform.BaseMeshU import BaseMeshU


def load_mesh(filename):
    vertices = []
    faces = []
    with open(filename) as f:
        line = f.readline()
        vertices_aux = []
        while line:
            line_tokens = line.split()
            if line_tokens[0] == 'v':
                vertices_aux.append([float(x) for x in line_tokens[1:]])
            elif line_tokens[0] == 'f':
                faces.append([int(x.split('/')[0]) - 1 for x in line_tokens[1:]])
            line = f.readline()
        for face in faces:
            for vertex_index in face:
                vertices.append(vertices_aux[vertex_index])
        print(f'Loaded {len(vertices)} {len(faces)}')
    return vertices, faces


class ObjMovingMesh(BaseMovingMesh):
    def __init__(self, program_id, filename):
        vertices, faces = load_mesh(filename)
        colors = []
        for i in range(len(vertices)):
            colors.append([random.random(), random.random(), random.random()])
        draw_type_aux = GL_TRIANGLES if len(faces[0]) == 3 else GL_QUADS
        super().__init__(program_id, vertices, colors, draw_type_aux)
