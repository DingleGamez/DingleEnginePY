from OpenGL.GL import *
import os

class Shader:
    def __init__(self):
        self.shaderProgram = None

    def use(self):
        glUseProgram(self.shaderProgram)

    def detach(self):
        glUseProgram(0)

    def loadShaderSource(self, path):
        if not os.path.isfile(path):
            raise FileNotFoundError(f"Shader file not found: {path}")
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()

    def compileShader(self, source, shaderType):
        shader = glCreateShader(shaderType)
        glShaderSource(shader, source)
        glCompileShader(shader)

        result = glGetShaderiv(shader, GL_COMPILE_STATUS)
        if not result:
            error = glGetShaderInfoLog(shader).decode()
            shaderTypeStr = "VERTEX" if shaderType == GL_VERTEX_SHADER else "FRAGMENT"
            raise RuntimeError(f"{shaderTypeStr} SHADER COMPILE ERROR:\n{error}")
        return shader

    def compile(self, vertexPath, fragmentPath):
        vertexShaderSource = self.loadShaderSource(vertexPath if vertexPath else "Engine/Resources/Shaders/DefaultVertex.glsl")
        fragmentShaderSource = self.loadShaderSource(fragmentPath if fragmentPath else "Engine/Resources/Shaders/DefaultFragment.glsl")
        vertexShader = self.compileShader(vertexShaderSource, GL_VERTEX_SHADER)
        fragmentShader = self.compileShader(fragmentShaderSource, GL_FRAGMENT_SHADER)

        self.shaderProgram = glCreateProgram()
        glAttachShader(self.shaderProgram, vertexShader)
        glAttachShader(self.shaderProgram, fragmentShader)
        glLinkProgram(self.shaderProgram)
        glDeleteShader(vertexShader)
        glDeleteShader(fragmentShader)

    def uploadMat4(self, name, mat):
        location = glGetUniformLocation(self.shaderProgram, name)
        glUniformMatrix4fv(location, 1, GL_FALSE, mat)

    def uploadTexture(self, name, array):
        location = glGetUniformLocation(self.shaderProgram, name)
        glUniform1i(location, array)