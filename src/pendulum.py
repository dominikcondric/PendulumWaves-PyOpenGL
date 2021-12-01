from shader import Shader
from entities import *

class Pendulum:
    def __init__(self) -> None:
        self.spheres = [Sphere() for i in range(10)]
        move = 9.
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
        self.construction_cubes[3].scale(glm.vec3(1., 1., 3.))
        self.construction_cubes[3].translate(glm.vec3(9.75, -7., 0.))
        self.construction_cubes[4].scale(glm.vec3(1., 1., 3.))
        self.construction_cubes[4].translate(glm.vec3(-9.75, -7., 0.))

        self.connecting_lines = [Line() for i in range(10)]
        move = 9.
        for line in self.connecting_lines:
            line.transform_matrix[3] = glm.vec4(move, 0., 0., 0.)
            line.transform_matrix[2] = glm.vec4(move, -4., 0., 0.)
            move -= 2.0
        
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

        shader.update_uniform_int("isLine", True)
        for line in self.connecting_lines:
            shader.update_uniform_mat4("model", line.transform_matrix)
            line.render()
        shader.update_uniform_int("isLine", False)

    def apply_physics(self) -> None:
        pass