import pygame
from pygame.locals import *
from OpenGL.GL import * # Módulo de PyOpenGL que proporciona acceso a las funciones de gráficos OpenGL.
from OpenGL.GLU import * # Módulo de PyOpenGL que proporciona funciones de utilidad de OpenGL, como la configuración de la perspectiva de la cámara.
from Cube import wireCube

# Este código es un ejemplo de cómo utilizar Pygame y OpenGL para crear una ventana en la que se renderiza un cubo en 3D.
# Inicializa PyGame
pygame.init()

# Configura la ventana con OpenGL
screen_width = 1000
screen_height = 800
# En OpenGL, los colores suelen especificarse como un conjunto de cuatro valores, correspondientes a los componentes
# rojo, verde, azul y alfa (RGBA), cada uno en el rango de 0.0 a 1.0. El componente alfa representa la transparencia,
# donde 0.0 es completamente transparente y 1.0 es completamente opaco.
# Esta tupla define el color de fondo de la ventana de renderizado.
# Se utiliza esta tupla en la función glClearColor(), que establece el color utilizado por glClear() para limpiar
# el color del buffer.
# Se establece a negro (0, 0, 0) con opacidad completa (1). Lo puse rosadito para probar.
background_color = (1, 0.2, 0.4, 1)
# Define el color de dibujo, en este caso, blanco (1, 1, 1) con opacidad completa (1). Este color se utiliza para los
# objetos que se van a dibujar en la ventana de renderizado.
# Para aplicar el color de dibujo, se usaría la función glColor3f() (para colores sin alfa) o glColor4f() (para colores
# con alfa) antes de dibujar los objetos.
drawing_color = (1, 1, 1, 1)

# Configurar la ventana de visualización usando Pygame con soporte de OpenGL para gráficos 3D
# pygame.display.set_mode(): Esta función inicializa una ventana o pantalla para el despliegue. (screen_width,
# screen_height): Define las dimensiones de la ventana en píxeles. DOUBLEBUF | OPENGL: Son banderas que se pasan a
# set_mode() para especificar opciones adicionales para la ventana. DOUBLEBUF: Habilita el "doble buffering". Esto
# significa que Pygame usará dos buffers para el renderizado: mientras uno se muestra en la pantalla, el otro se
# puede usar para dibujar el siguiente cuadro. Esto es esencial para las animaciones suaves, especialmente en
# aplicaciones 3D con OpenGL. OPENGL: Indica que la ventana debe ser creada con soporte para gráficos OpenGL. Esto
# permite utilizar las funciones de OpenGL para renderizar gráficos 3D en la ventana creada por Pygame.
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
#  Estableciendo el Título de la Ventana
pygame.display.set_caption('OpenGL in Python')


def initialise():
    # glClearColor(): Establece el color utilizado por glClear() para limpiar el color del buffer.
    glClearColor(background_color[0], background_color[1], background_color[2], background_color[3])
    # glColor(): Establece el color de dibujo actual. Este color se utiliza para los objetos que se van a dibujar en
    # la ventana de renderizado.
    glColor(drawing_color)

    # Configuración de la perspectiva de la cámara
    # glMatrixMode(): Esta función define cuál de las matrices de OpenGL
    # será el objetivo de las operaciones subsiguientes de matriz (por ejemplo, transformaciones).
    # GL_PROJECTION: Este parámetro indica que las operaciones de matriz subsecuentes afectarán la matriz de proyección.
    # La matriz de proyección se utiliza para configurar la cámara de la escena 3D, incluyendo cómo se mapea la escena
    # 3D a las coordenadas de la pantalla, esencialmente definiendo el campo de visión, la relación de aspecto, y los
    # planos cercano y lejano de recorte.
    glMatrixMode(GL_PROJECTION)
    # glLoadIdentity(): Restablece la matriz actual al estado predeterminado (la matriz identidad). Es útil para
    # eliminar cualquier transformación previa y asegurarse de que la configuración de la proyección no esté
    # influenciada por operaciones de matriz anteriores. En el contexto de GL_PROJECTION, prepara la matriz para
    # definir una nueva proyección desde una base limpia.
    glLoadIdentity()
    # gluPerspective(): Esta función define una matriz de proyección en perspectiva que simula la percepción de
    # profundidad como lo hace el ojo humano. Por lo tanto, los objetos más cercanos aparecen más grandes que los que
    # están más lejos. El primer parámetro 60 especifica el ángulo de visión en el eje vertical (campo de visión) en
    # grados, lo que afecta cuán "profundo" y "amplio" se puede ver en la escena 3D. El segundo parámetro (
    # screen_width / screen_height) calcula la relación de aspecto de la ventana, asegurando que no haya distorsión
    # en la imagen independientemente de las dimensiones de la ventana. Los dos últimos parámetros, 0.1 y 100.0,
    # definen los planos de recorte cercano y lejano, respectivamente. Estos parámetros limitan qué tan cerca y qué
    # tan lejos puede estar un objeto de la cámara para ser renderizado. Los objetos fuera de este rango no se
    # dibujarán.
    gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)
    # gluPerspective(Entre mayor sea el número de grados, más amplio será el campo de visión)

    # Configuración del Modelview: Establece cómo se visualizarán los objetos dentro de la ventana de renderizado
    # glMatrixMode(): Especifica la matriz actual que OpenGL usará para las transformaciones. GL_MODELVIEW: Este modo
    # se utiliza para definir y modificar la matriz de modelo-vista, que combina la matriz de modelo (
    # transformaciones aplicadas a los objetos) y la matriz de vista (transformaciones aplicadas a la cámara o punto
    # de vista)
    glMatrixMode(GL_MODELVIEW)
    # glLoadIdentity(): Restablece la matriz actual al estado predeterminado (la matriz identidad). Es útil para
    # eliminar cualquier transformación previa y asegurarse de que la configuración de la proyección no esté
    # influenciada por operaciones de matriz anteriores. En el contexto de GL_MODELVIEW, prepara la matriz para
    # definir una nueva transformación de modelo-vista desde una base limpia.
    glLoadIdentity()
    # Aplica una transformación de traslación a la matriz actual. En este caso, mueve todos los objetos en la escena
    # 5 unidades hacia atrás a lo largo del eje Z.
    glTranslate(0, 0, -2)
    # glViewport(): Define la porción de la ventana donde OpenGL dibujará los gráficos. Los primeros dos parámetros (
    # 0, 0) indican la esquina inferior izquierda del viewport, y los últimos dos (screen.get_width(),
    # screen.get_height()) definen el ancho y alto del viewport. Esta función asegura que OpenGL utilice toda la
    # ventana para el renderizado.
    glViewport(0, 0, screen.get_width(), screen.get_height())
    # glEnable(): Habilita ciertas capacidades de OpenGL, en este caso, el test de profundidad. GL_DEPTH_TEST: Cuando
    # está habilitado, OpenGL realiza comparaciones de profundidad y actualiza el buffer de profundidad. Esto es
    # crucial para renderizar correctamente los objetos en 3D, asegurando que los objetos más cercanos no sean
    # ocultados por aquellos que están más lejos de la vista.
    glEnable(GL_DEPTH_TEST)


def display():
    # glClear(): Esta función limpia los buffers a valores predefinidos. Los buffers son áreas de memoria usadas para
    # almacenar datos de píxeles de la imagen o la profundidad de los objetos en la escena. GL_COLOR_BUFFER_BIT:
    # Indica que el buffer de color (donde se almacena la imagen que se va a mostrar) debe ser limpiado. Esto prepara
    # el área de dibujo rellenándola con el color definido previamente por glClearColor(). GL_DEPTH_BUFFER_BIT:
    # Indica que el buffer de profundidad (que se usa para determinar si un objeto está delante o detrás de otro)
    # también debe ser limpiado. Esto es crucial para renderizar correctamente la escena 3D, permitiendo que los
    # objetos más cercanos oculten a los más lejanos.
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # glRotatef(): Aplica una rotación a la matriz de transformación actual. Esta función es utilizada para rotar
    # objetos en la escena. El primer argumento (1) especifica el ángulo de rotación en grados. Entre mayor sea el
    # número más rapido se hace la rotación.
    # Los siguientes tres argumentos (10, 0, 1) especifican el vector de eje alrededor del cual se realizará la
    # rotación. En este caso, la rotación se hace en una dirección que es una combinación del eje X (10% hacia x)
    # y el eje Z (100% hacia z), lo que crea un efecto de rotación inclinada.
    # Esta línea hace que to-do lo que se dibuje después (hasta que se modifique la matriz de transformación
    # nuevamente) se rote según estos parámetros.
    glRotatef(1, 10, 0, 1)
    # glPushMatrix(): Guarda una copia de la matriz de transformación actual en el stack de matrices. Esto se utiliza
    # para conservar el estado actual de las transformaciones (como la posición, rotación, y escala) antes de aplicar
    # nuevas transformaciones.
    glPushMatrix()
    # wireCube(): Esta es una llamada a una función definida por el usuario (no estándar de OpenGL) que
    # presumiblemente dibuja un cubo en modo de alambre. Entre glPushMatrix() y glPopMatrix(), las transformaciones
    # que se aplican afectan solo a las operaciones de dibujo realizadas entre estas llamadas.
    wireCube()
    # Restaura la matriz de transformación al estado anterior guardado por la última llamada a glPushMatrix(). Esto
    # permite que las transformaciones aplicadas después de glPushMatrix() no afecten a las operaciones de dibujo
    # futuras fuera de este bloque.
    glPopMatrix()

# Esta variable se usa como una bandera para controlar el bucle principal del programa. Mientras done sea False,
# el programa continuará ejecutándose.
done = False
initialise()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    display()
    # Actualiza la pantalla con lo que se ha dibujado. En el contexto de Pygame con doble buffering (habilitado por
    # DOUBLEBUF), pygame.display.flip() intercambia los buffers: el buffer en el que se ha estado dibujando se
    # muestra en la pantalla, y el buffer visible anteriormente se convierte en el buffer de dibujo.
    pygame.display.flip()
    # Hace una pausa en la ejecución del programa por un corto tiempo (100 milisegundos en este caso) para limitar la
    # velocidad a la que se ejecuta el bucle principal. Esto es útil para no consumir más recursos de CPU de los
    # necesarios y para controlar la tasa de refresco de la pantalla.
    pygame.time.wait(100)
# Se llama una vez que el bucle principal termina (cuando done es True). Esta función cierra la ventana de Pygame y
# termina cualquier proceso de Pygame que se esté ejecutando. Es una buena práctica llamar a pygame.quit() para
# asegurar que el programa se cierra limpiamente.
pygame.quit()