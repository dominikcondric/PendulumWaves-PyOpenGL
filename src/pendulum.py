from shader import Shader
from entities import *

class Pendulum:
    def __init__(self, string_starting_position: glm.vec3, string_len: float, initial_angle: float = glm.pi() / 4.) -> None:
        self.string_length = string_len
        self.angle = initial_angle
        self.angular_velocity = 0.

        self.string = Line()
        self.string.color = glm.vec4(1., 0., 0., 1.)
        self.string.transform_matrix[3] = glm.vec4(string_starting_position.x, 0., string_starting_position.z, 1.)
        self.sphere = Sphere()
        self.sphere.translate(glm.vec3(string_starting_position.x, 0., 0.))
        self.updateTranslationBasedOnAngle()

    def updateTranslationBasedOnAngle(self) -> None:
        sphere_position = glm.vec3(self.sphere.translation_vector.x, -np.cos(self.angle) * self.string_length * 10, np.sin(self.angle) * self.string_length * 10)
        self.string.transform_matrix[2] = glm.vec4(sphere_position, 1.0)
        self.sphere.translate(sphere_position)

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

    def apply_physics(self, delta_time: float) -> None:
        def pendulum_equation():
            return -(9.81 / (self.string_length)) * np.sin(self.angle)

        # Explicit Euler integration
        angular_acceleration = pendulum_equation()
        self.angular_velocity += angular_acceleration * delta_time
        self.angle += self.angular_velocity * delta_time
        self.updateTranslationBasedOnAngle()        