from shader import Shader
from entities import *
from scipy import integrate as intg

class Pendulum:
    def __init__(self, sphere_position: glm.vec3, string_len: float) -> None:
        self.string_length = string_len
        self.angle = 0
        self.sphere = Sphere()
        self.sphere.translate(glm.vec3(sphere_position))

        self.string = Line()
        self.string.color = glm.vec4(1., 0., 0., 1.)
        self.string.transform_matrix[3] = glm.vec4(sphere_position.x, sphere_position.y + string_len, sphere_position.z, 1.)
        self.string.transform_matrix[2] = glm.vec4(sphere_position.x, sphere_position.y, sphere_position.z, 1.)
        
    def draw(self, shader: Shader) -> None:
        shader.use()
        shader.update_uniform_int("lightened", self.sphere.lightened)
        shader.update_uniform_vec4("material.color", self.sphere.color)
        shader.update_uniform_mat4("model", self.sphere.transform_matrix)
        self.sphere.render()

        shader.update_uniform_int("isLine", True)
        shader.update_uniform_vec4("material.color", self.string.color)
        shader.update_uniform_mat4("model", self.string.transform_matrix)
        self.string.render()
        shader.update_uniform_int("isLine", False)

    def apply_physics(self) -> None:
        def pendulumEquation(string_length, angle):
            return -(9.81 / string_length) * np.sin(angle)
        pass
        


        

        