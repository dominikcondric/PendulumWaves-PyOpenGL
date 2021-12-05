from shader import Shader
from entities import *
from pendulum import Pendulum
import glm

class PendulumSystem:
    def __init__(self) -> None:
        self.pendulums = []
        pendulum_position = 9.
        pendulum_string_length = 5
        for i in range(10):
            self.pendulums.append(Pendulum(glm.vec3(pendulum_position, -pendulum_string_length, 0.), pendulum_string_length))
            self.pendulums[i].sphere.color = glm.vec4(1., 0.25, 0., 1.)
            pendulum_position -= 2.0
            pendulum_string_length -= 0.2

        self.construction_cubes = [Cube() for i in range(5)]
        self.construction_cubes[0].scale(glm.vec3(19., 0.5, 0.5))
        self.construction_cubes[0].color = glm.vec4(0.2, 0.2, 0.2, 1.)
        self.construction_cubes[1].scale(glm.vec3(0.5, 7., 0.5))
        self.construction_cubes[1].translate(glm.vec3(9.75, -3.25, 0.))
        self.construction_cubes[2].scale(glm.vec3(0.5, 7., 0.5))
        self.construction_cubes[2].translate(glm.vec3(-9.75, -3.25, 0.))
        self.construction_cubes[3].scale(glm.vec3(1., 1., 3.))
        self.construction_cubes[3].translate(glm.vec3(9.75, -7., 0.))
        self.construction_cubes[4].scale(glm.vec3(1., 1., 3.))
        self.construction_cubes[4].translate(glm.vec3(-9.75, -7., 0.))
        
    def draw(self, shader: Shader) -> None:
        shader.use()
        shader.update_uniform_int("lightened", self.construction_cubes[0].lightened)
        shader.update_uniform_vec4("material.color", self.construction_cubes[0].color)
        for cube in self.construction_cubes:
            shader.update_uniform_mat4("model", cube.transform_matrix)
            cube.render()

        for pendulum in self.pendulums:
            pendulum.draw(shader)

    def apply_physics(self) -> None:
        for pendulum in self.pendulums:
            pendulum.apply_physics()
        

        