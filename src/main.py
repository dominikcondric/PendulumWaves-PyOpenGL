from pendulumSystem import PendulumSystem
from window import Window
import glm
from OpenGL.GL import *
from shader import Shader
from camera import PerspectiveCamera
from entities import *
import time 
import glfw

def main():
    window = Window(1024, 768, "Pendulum Waves")
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)
    glViewport(0, 0, 1024, 768)
    shader = Shader("GeneralVertexShader.glsl", "GeneralFragmentShader.glsl")
    cam = PerspectiveCamera(glm.vec3(20., -2., 0.))
    cam.center.y = -2.
    light_source = Sphere()
    light_source.scale(glm.vec3(0.2))
    light_source.translate(glm.vec3(-2., 1., 1))
    light_source.lightened = False

    pendulumSystem = PendulumSystem()
    clearing_color = glm.vec4(0.1, 0.1, 0.1, 1.0)
    glClearColor(clearing_color.r, clearing_color.g, clearing_color.b, clearing_color.a)

    shader.use()
    shader.update_uniform_float("material.ambientCoefficient", 0.1)
    shader.update_uniform_float("material.diffuseCoefficient", 0.9)
    shader.update_uniform_float("material.specularCoefficient", 0.8)
    shader.update_uniform_float("material.shininess", 50.)
    shader.update_uniform_vec3("eyePosition", cam.position)
    shader.update_uniform_vec3("light.position", light_source.translation_vector)
    shader.update_uniform_vec3("light.color", glm.vec3(light_source.color))

    window.update_time()
    while not window.should_close():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        shader.update_uniform_mat4("view", cam.lookAt())
        shader.update_uniform_mat4("projection", cam.project())
        # Light source rendering
        shader.update_uniform_vec4("material.color", light_source.color)
        shader.update_uniform_mat4("model", light_source.transform_matrix)
        shader.update_uniform_int("lightened", light_source.lightened)
        light_source.render()

        # Pendulum rendering
        if np.abs(window.last_delta_time - window.delta_time) < 0.02:
            pendulumSystem.apply_physics(window.delta_time)
        pendulumSystem.draw(shader)

        window.swap_buffers()
        window.poll_events()

        if window.resized:
            win_width, win_height = window.get_window_size()
            if win_width != 0 and win_height != 0:
                cam.aspect_ratio = float(win_width) / win_height
            glViewport(0, 0, win_width, win_height)
            window.update_time()

        window.update_time()
        if window.delta_time < 1. / 60:
            time.sleep((1. / 60 - window.delta_time) / 2)
            window.update_time()            

# start of the program
if __name__ == "__main__":
    main()
    
