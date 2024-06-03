from OpenGL.GL import *

# Esta lista vertices contiene tuplas que representan las coordenadas (x, y, z) de los vértices del cubo. Los
# vértices se definen en un espacio tridimensional.
vertices = [(0.5, -0.5, 0.5),
            (-0.5, -0.5, 0.5),
            (0.5, 0.5, 0.5),
            (-0.5, 0.5, 0.5),
            (0.5, 0.5, -0.5),
            (-0.5, 0.5, -0.5),
            (0.5, -0.5, -0.5),
            (-0.5, -0.5, -0.5),
            (0.5, 0.5, 0.5),
            (-0.5, 0.5, 0.5),
            (0.5, 0.5, -0.5),
            (-0.5, 0.5, -0.5),
            (0.5, -0.5, -0.5),
            (0.5, -0.5, 0.5),
            (-0.5, -0.5, 0.5),
            (-0.5, -0.5, -0.5),
            (-0.5, -0.5, 0.5),
            (-0.5, 0.5, 0.5),
            (-0.5, 0.5, -0.5),
            (-0.5, -0.5, -0.5),
            (0.5, -0.5, -0.5),
            (0.5, 0.5, -0.5),
            (0.5, 0.5, 0.5),
            (0.5, -0.5, 0.5)
            ]
# Contiene índices de los vértices que forman triángulos. Cada grupo de tres números representa un triángulo,
# donde cada número es un índice en la lista vertices
triangles = [0, 2, 3, 0, 3, 1, 8, 4, 5, 8, 5, 9, 10, 6, 7, 10, 7, 11, 12,
             13, 14, 12, 14, 15, 16, 17, 18, 16, 18, 19, 20, 21, 22, 20, 22, 23]


def wireCube():
    for t in range(len(triangles) - 3):
        # Inicia el dibujo de líneas.
        glBegin(GL_LINES)
        # Especifica un vértice en el espacio 3D. Cada llamada a glVertex3fv con un vértice de la lista vertices
        # indica un punto de inicio o fin de una línea.
        glVertex3fv(vertices[triangles[t]])
        # Las llamadas consecutivas a glVertex3fv definen las líneas del cubo. Cada par de vértices define una línea.
        glVertex3fv(vertices[triangles[t + 1]])
        glVertex3fv(vertices[triangles[t + 2]])
        # Termina el dibujo de líneas.
        glEnd()
        t += 3

