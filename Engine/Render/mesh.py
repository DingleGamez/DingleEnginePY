from engine.render.texture import Texture

from OpenGL.GL import *

class Mesh:
    def __init__(self, vertices, indices, normals, texcoords, color):
        self.vertices = vertices
        self.indices = indices
        self.normals = normals
        self.texcoords = texcoords
        self.texture = Texture(None, color)
        self.vao, self.vao, self.ebo = None, None, None

        self.setup_mesh()

    def setup_mesh(self):
        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)

        vertice_vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vertice_vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(0)

        normal_vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, normal_vbo)
        glBufferData(GL_ARRAY_BUFFER, self.normals.nbytes, self.normals, GL_STATIC_DRAW)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(1)

        texcoords_vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, texcoords_vbo)
        glBufferData(GL_ARRAY_BUFFER, self.texcoords.nbytes, self.texcoords, GL_STATIC_DRAW)
        glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(2)

        ebo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.indices.nbytes, self.indices, GL_STATIC_DRAW)

        glBindVertexArray(0)

        self.texture.start()

    def draw(self, shader):
        self.texture.bind()
        shader.upload_texture("texSampler", 0)

        glBindVertexArray(self.vao)
        glDrawElements(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, None)
        glBindVertexArray(0)

        glActiveTexture(GL_TEXTURE0)