from OpenGL.GL import *

class Shader:
    def __init__(self):
        self.shaderProgram = None
        self.vertexShaderSource = """
        #version 330 core
        layout (location = 0) in vec3 aPos;
        layout (location = 1) in vec2 aTexCoord;

        uniform mat4 model;
        uniform mat4 view;
        uniform mat4 projection;

        out vec2 TexCoord;

        void main() 
        {
            gl_Position = projection * view * model * vec4(aPos, 1.0);
            
            TexCoord = aTexCoord;
        }
        """
        self.fragmentShaderSource = """
        #version 330 core
        out vec4 FragColor;

        in vec2 TexCoord;

        uniform sampler2D texSampler;

        void main() 
        {
            FragColor = texture(texSampler, TexCoord);
            if(FragColor.a < 0.1)
                discard;
        }
        """

    def use(self):
        glUseProgram(self.shaderProgram)

    def detach(self):
        glUseProgram(0)


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

    def compile(self):
        vertexShader = self.compileShader(self.vertexShaderSource, GL_VERTEX_SHADER)
        fragmentShader = self.compileShader(self.fragmentShaderSource, GL_FRAGMENT_SHADER)

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