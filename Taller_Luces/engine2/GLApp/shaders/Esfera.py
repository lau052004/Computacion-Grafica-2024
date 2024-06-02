import pygame
from OpenGL.GL import *
import numpy as np
from engine2.GLApp.BaseApps.BaseScene import BaseScene
from engine2.GLApp.Camera.Camera import Camera
from engine2.GLApp.Mesh.Uniform.AxesU import AxesU
from engine2.GLApp.Mesh.Uniform.SphereU import SphereU
from engine2.GLApp.Utils.Utils import create_program

vertex_shader = r'''
#version 330 core

in vec3 position;
in vec3 vertexColor;
in vec3 vertexNormal;
uniform mat4 projectionMatrix;
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;

out vec3 color;
out vec3 normal;
out vec3 fragPos;
out vec3 viewPos;

void main()
{
    gl_Position = projectionMatrix * inverse(viewMatrix) * modelMatrix * vec4(position, 1);
    normal = mat3(transpose(inverse(modelMatrix))) * vertexNormal;
    fragPos = vec3(modelMatrix * vec4(position, 1));
    color = vertexColor;
    viewPos = vec3(inverse(viewMatrix) * vec4(0, 0, 0, 1)); // Corregido para calcular la posición de la vista correctamente
}

'''

fragment_shader = r'''
#version 330 core

in vec3 color;
in vec3 normal;
in vec3 fragPos;
in vec3 viewPos;
uniform vec3 lightPositions[3];
uniform vec3 lightColors[3];

out vec4 fragColor;

void main() {
    vec3 result = vec3(0.0); // Resultado final de la iluminación
    vec3 ambientComponent = vec3(0.1); // Componente ambiental básico
    
    for(int i = 0; i < 3; i++) {
        vec3 lightDirection = normalize(lightPositions[i] - fragPos);
        float diff = max(dot(normal, lightDirection), 0.0);
        vec3 diffuse = diff * lightColors[i];
        
        vec3 viewDir = normalize(viewPos - fragPos);
        vec3 reflectDir = reflect(-lightDirection, normal);
        float spec = pow(max(dot(viewDir, reflectDir), 0.0), 32);
        vec3 specular = 0.5 * spec * lightColors[i];
        
        result += ambientComponent + diffuse + specular;
    }
    
    fragColor = vec4(color * result, 1.0); // Corregido para aplicar el color correctamente
}

'''


class VertexShaderCameraDemo(BaseScene):
    def __init__(self):
        super().__init__(1000, 800)
        self.angle = 0  # Ángulo inicial para la rotación de las luces

    def initialize(self):
        super().initialize()
        self.program_id = create_program(vertex_shader, fragment_shader)
        self.lights = [
            {"position": [-5.0, 5.0, 5.0], "color": [0.0, 1.0, 0.0]},
            {"position": [-5.0, -5.0, 5.0], "color": [0.0, 0.0, 1.0]}
        ]
        self.square = SphereU(self.program_id, [0, 0, 0])
        self.axes = AxesU(self.program_id, pygame.Vector3(0, 0, 0))
        self.camera = Camera(self.program_id, self.screen.get_width(), self.screen.get_height())
        glEnable(GL_DEPTH_TEST)

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_id)

        # Rotar las luces alrededor de la esfera
        radius = 20.0
        self.angle += 0.005
        self.lights[0]['position'] = [np.cos(self.angle) * radius, 5.0, np.sin(self.angle) * radius]
        self.lights[1]['position'] = [np.cos(self.angle + np.pi) * radius, -5.0, np.sin(self.angle + np.pi) * radius]

        # Actualizar las posiciones de las luces en los shaders
        for i, light in enumerate(self.lights):
            glUniform3fv(glGetUniformLocation(self.program_id, f'lightPositions[{i}]'), 1, light["position"])
            glUniform3fv(glGetUniformLocation(self.program_id, f'lightColors[{i}]'), 1, light["color"])

        self.camera.update()
        self.square.draw()
        self.axes.draw()

if __name__ == '__main__':
    pygame.init()
    demo = VertexShaderCameraDemo()
    demo.main_loop()
    pygame.quit()
