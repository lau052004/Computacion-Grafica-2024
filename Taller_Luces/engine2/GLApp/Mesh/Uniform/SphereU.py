from OpenGL.GL import *
import numpy as np

from engine2.GLApp.Mesh.Uniform.BaseMeshU import BaseMeshU


class SphereU(BaseMeshU):
    def __init__(self, program_id, location):
        self.vertices = self.generate_sphere_vertices()
        self.colors = self.generate_vertex_colors()
        self.normals = self.generate_sphere_normals()
        super().__init__(program_id, self.vertices, self.colors, GL_TRIANGLE_FAN, translation=location)

    def generate_sphere_normals(self):
        normals = []
        for vertex in self.vertices:
            normal = np.array(vertex)  # Convert vertex to a numpy array if it's not already
            normalized_normal = normal / np.linalg.norm(normal)  # Normalizar el vector
            normals.append(normalized_normal)
        return normals

    def generate_sphere_vertices(self, radius=1.0, lat_steps=200, lon_steps=200):
        vertices = []
        for i in range(lat_steps + 1):
            lat = np.pi * i / lat_steps
            for j in range(lon_steps + 1):
                lon = 2 * np.pi * j / lon_steps
                x = radius * np.sin(lat) * np.cos(lon)
                y = radius * np.sin(lat) * np.sin(lon)
                z = radius * np.cos(lat)
                vertices.append([x, y, z])
        return vertices

    def generate_vertex_colors(self):
        # Aquí se podría definir una lógica para colorear los vértices basada en su posición
        # Para este ejemplo, todos los vértices serán blancos por simplicidad
        return [[1, 1, 1] for _ in self.vertices]

