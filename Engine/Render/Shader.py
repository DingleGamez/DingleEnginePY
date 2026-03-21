from pathlib import Path

from pyglm import glm
from OpenGL.GL import *

class Shader:
    def __init__(self, path):
        self.path = path
        self.vertex_src = None
        self.fragment_src = None
        self.shader_program = None

        self.start()

    def use(self):
        glUseProgram(self.shader_program)

    def detach(self):
        glUseProgram(0)

    def start(self):
        path = self.path.split(".")

        vert_path = Path(path[0] + "_vert." + path[1])
        if not vert_path.exists(): raise FileNotFoundError(f"Shader file not found: {vert_path}")
        vert_src = vert_path.read_text()

        frag_path = Path(path[0] + "_frag." + path[1])
        if not frag_path.exists(): raise FileNotFoundError(f"Shader file not found: {frag_path}")
        frag_src = frag_path.read_text()

        self.vertex_src = vert_src
        self.fragment_src = frag_src

    def compile(self):
        vertex_shader = glCreateShader(GL_VERTEX_SHADER)
        glShaderSource(vertex_shader, self.vertex_src)
        glCompileShader(vertex_shader)

        fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)
        glShaderSource(fragment_shader, self.fragment_src)
        glCompileShader(fragment_shader)

        self.shader_program = glCreateProgram()
        glAttachShader(self.shader_program, vertex_shader)
        glAttachShader(self.shader_program, fragment_shader)
        glLinkProgram(self.shader_program)
        glDeleteShader(vertex_shader)
        glDeleteShader(fragment_shader)

    def upload_mat4(self, name, data):
        location = glGetUniformLocation(self.shader_program, name)
        glUniformMatrix4fv(location, 1, GL_FALSE, glm.value_ptr(data))

    def upload_texture(self, name, data):
        location = glGetUniformLocation(self.shader_program, name)
        glUniform1i(location, data)

    def upload_vec3v(self, name, data):
        location = glGetUniformLocation(self.shader_program, name)
        glUniform3fv(location, 1, glm.value_ptr(data))

    def upload_vec3(self, name, x, y, z):
        location = glGetUniformLocation(self.shader_program, name)
        glUniform3f(location, x, y, z)