import ctypes
from logging import info
from re import S
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import glm

class Shader:
    def __init__(self, vertexShaderName: str, fragmentShaderName: str):
        self.uniform_cache = dict()
        self._create_shader_program(vertexShaderName, fragmentShaderName)

    def _create_shader_program(self, vertexShaderName: str, fragmentShaderName: str):
        with open("Shaders/" + vertexShaderName, 'r') as file:
            vertex_shader_code = file.read()
            file.close()

        with open("Shaders/" + fragmentShaderName, 'r') as file:
            fragment_shader_code = file.read()
            file.close()

        vertex_shader_ID = compileShader(vertex_shader_code, GL_VERTEX_SHADER)
        fragment_shader_ID = compileShader(fragment_shader_code, GL_FRAGMENT_SHADER)

        self.program_ID = compileProgram(vertex_shader_ID, fragment_shader_ID)

    def __del__(self):
        glDeleteProgram(self.program_ID)

    def use(self):
        glUseProgram(self.program_ID)

    def _get_uniform_location(self, uniform_name: str) -> int:
        if uniform_name in self.uniform_cache:
            return self.uniform_cache[uniform_name]
        else:
            self.uniform_cache[uniform_name] = glGetUniformLocation(self.program_ID, uniform_name)
            return self.uniform_cache[uniform_name]

    def update_uniform_mat4(self, uniform_name: str, mat4: glm.mat4) -> None:
        values = []
        for i in range(4):
            for j in range(4):
                values.append(mat4[i][j])

        glUniformMatrix4fv(self._get_uniform_location(uniform_name), 1, GL_FALSE, values)

    def update_uniform_vec3(self, uniform_name: str, vec3: glm.vec3) -> None:
        glUniform3f(self._get_uniform_location(uniform_name), vec3.x, vec3.y, vec3.z)

    def update_uniform_vec4(self, uniform_name: str, vec4: glm.vec4) -> None:
        glUniform4f(self._get_uniform_location(uniform_name), vec4.x, vec4.y, vec4.z, vec4.w)

    def update_uniform_int(self, uniform_name: str, value: int) -> None:
        glUniform1i(self._get_uniform_location(uniform_name), value)

    def update_uniform_float(self, uniform_name: str, value: float) -> None:
        glUniform1f(self._get_uniform_location(uniform_name), value)



                
        
        