from shader import Shader
from entities import *

class Pendulum:
    def __init__(self) -> None:
        self.spheres = [Sphere() for i in range(10)]
        move = 9
        for sphere in self.spheres:
            sphere.translate(glm.vec3(move, -4., 0.))
            sphere.color = glm.vec4(1., 0.25, 0., 1.)
            move -= 2.0

        self.construction_cubes = [Cube() for i in range(5)]
        self.construction_cubes[0].scale(glm.vec3(19., 0.5, 0.5))
        self.construction_cubes[0].color = glm.vec4(0.2, 0.2, 0.2, 1.)
        self.construction_cubes[1].scale(glm.vec3(0.5, 7., 0.5))
        self.construction_cubes[1].translate(glm.vec3(9.75, -3.25, 0.))
        self.construction_cubes[2].scale(glm.vec3(0.5, 7., 0.5))
        self.construction_cubes[2].translate(glm.vec3(-9.75, -3.25, 0.))
        
    def draw(self, shader: Shader) -> None:
        shader.use()
        shader.update_uniform_int("lightened", self.construction_cubes[0].lightened)
        shader.update_uniform_vec4("material.color", self.construction_cubes[0].color)
        for cube in self.construction_cubes:
            shader.update_uniform_mat4("model", cube.transform_matrix)
            cube.render()

        shader.update_uniform_int("lightened", self.spheres[0].lightened)
        shader.update_uniform_vec4("material.color", self.spheres[0].color)
        for sphere in self.spheres:
            shader.update_uniform_mat4("model", sphere.transform_matrix)
            sphere.render()

    def apply_physics(self) -> None:
        pass