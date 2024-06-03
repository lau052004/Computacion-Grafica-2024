import numpy as np
from OpenGL.GL import *

colors = [
    (1.0, 0.0, 0.0),  # Rojo para colors[0]
    (0.0, 1.0, 0.0),  # Verde para colors[1]
    (0.0, 0.0, 1.0),  # Azul para colors[2]
    (1.0, 1.0, 0.0),  # Amarillo para colors[3]
    (1.0, 0.0, 1.0),  # Magenta para colors[4]
    (0.0, 1.0, 1.0)   # Cian para colors[5]
]

# Define una función para dibujar una malla paramétrica a partir de una matriz de puntos.
def plot_parametric_mesh(points_matrix):
    # Establece el tamaño de los puntos que se dibujarán a 3 píxeles.
    glPointSize(3)
    # Se resta uno para que para que se pueda usar un índice que empiece en 0.
    n_rows = len(points_matrix) - 1
    n_cols = len(points_matrix[0])
    # Itera a través de cada punto en la matriz para dibujar líneas entre ellos.
    for i in range(n_rows):
        for j in range(n_cols):
            glBegin(GL_LINES)
            glColor3fv(colors[3])
            glVertex3fv(points_matrix[i][j])
            # glColor3fv(colors[1])
            # El operador módulo asegurando que el índice se envuelva si es necesario (si j + 1 es igual al número de
            # columnas, se envuelve a 0).
            glVertex3fv(points_matrix[i][(j + 1) % n_cols])
            # glColor3fv(colors[2])
            # Establece otro color y define un vértice que conecta la siguiente fila i + 1 y la siguiente columna j +
            # 1, aplicando módulo a ambos índices
            glVertex3fv(points_matrix[(i + 1) % n_rows][(j + 1) % n_cols])
            #  glColor3fv(colors[0])
            #  Vuelve a establecer el color inicial y reespecifica el primer punto, cerrando la secuencia de líneas.
            glVertex3fv(points_matrix[i][j])
            glEnd()

            glBegin(GL_LINES)
            glColor3fv(colors[4])
            glVertex3fv(points_matrix[i][j])
            glVertex3fv(points_matrix[(i + 1) % n_rows][(j + 1) % n_cols])
            glVertex3fv(points_matrix[(i + 1) % n_rows][j])
            glVertex3fv(points_matrix[i][j])
            glEnd()


def generate_sphere_points(
        radius=3,
        alpha_samples=20,
        beta_samples=10
):
    point_matrix = []
    for alpha in np.linspace(0, 2 * np.pi, alpha_samples):
        point_array = []
        for beta in np.linspace(0, np.pi, beta_samples):
            point_array.append(
                (
                    radius * np.cos(alpha) * np.sin(beta),
                    radius * np.sin(alpha) * np.sin(beta),
                    radius * np.cos(beta)
                )
            )
        point_matrix.append(point_array)
    return point_matrix


def generate_toroid_points(
        radius_1=4,
        radius_2=1,
        alpha_samples=20,
        beta_samples=20
):
    # Crea una lista vacía llamada point_matrix, que se llenará con puntos que representan la superficie de la esfera.
    point_matrix = []
    # Generación de Puntos a lo Largo de la Longitud Inicia un bucle sobre alpha, que es el ángulo alrededor del eje
    # vertical (longitud). np.linspace genera alpha_samples números equidistantes entre 0 y 2 * np.pi (un círculo
    # completo).
    for alpha in np.linspace(0, 2 * np.pi, alpha_samples):
        # Inicialización del Array de Puntos para la Fila Actual
        point_array = []
        # Inicia un bucle anidado sobre beta, que es el ángulo desde el polo superior de la esfera hasta el inferior
        # (latitud). np.linspace genera beta_samples números equidistantes entre 0 y np.pi (un semicírculo).
        for beta in np.linspace(0, 2 * np.pi, beta_samples):
            point_array.append(
                (
                    (radius_1 + radius_2 * np.cos(beta)) * np.sin(alpha),
                    (radius_1 + radius_2 * np.cos(beta)) * np.cos(alpha),
                    radius_2 * np.sin(beta)
                )
            )
        # Agregar Fila de Puntos a la Matriz de Puntos Después de llenar point_array con puntos para un valor de
        # alpha específico, lo añade a point_matrix. Esto construye la matriz de puntos fila por fila, donde cada
        # fila corresponde a un valor fijo de alpha y cada columna a un valor de beta.
        point_matrix.append(point_array)
    return point_matrix
# La matriz resultante point_matrix es una representación de la superficie de una esfera en coordenadas cartesianas,
# donde cada fila de la matriz corresponde a una línea de latitud de la esfera y cada punto en la fila corresponde a
# un punto a lo largo de esa línea de latitud. La función puede ser utilizada para dibujar una esfera en 3D al
# conectar estos puntos con líneas o triángulos.