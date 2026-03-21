from engine.components.component import Component
from engine.render.texture import Texture

import numpy as np
from OpenGL.GL import *

class Mesh(Component):
    def __init__(self, tex_path=None):
        super().__init__()

        self.vertices = np.array([
            # FRONT (+Z)
            -0.5, -0.5, 0.5, 0.0, 0.0, 1.0, 0.0, 0.0,
            0.5, -0.5, 0.5, 0.0, 0.0, 1.0, 1.0, 0.0,
            0.5, 0.5, 0.5, 0.0, 0.0, 1.0, 1.0, 1.0,
            -0.5, 0.5, 0.5, 0.0, 0.0, 1.0, 0.0, 1.0,

            # BACK (-Z)
            -0.5, -0.5, -0.5, 0.0, 0.0, -1.0, 1.0, 0.0,
            0.5, -0.5, -0.5, 0.0, 0.0, -1.0, 0.0, 0.0,
            0.5, 0.5, -0.5, 0.0, 0.0, -1.0, 0.0, 1.0,
            -0.5, 0.5, -0.5, 0.0, 0.0, -1.0, 1.0, 1.0,

            # LEFT (-X)
            -0.5, 0.5, 0.5, -1.0, 0.0, 0.0, 1.0, 0.0,
            -0.5, 0.5, -0.5, -1.0, 0.0, 0.0, 1.0, 1.0,
            -0.5, -0.5, -0.5, -1.0, 0.0, 0.0, 0.0, 1.0,
            -0.5, -0.5, 0.5, -1.0, 0.0, 0.0, 0.0, 0.0,

            # RIGHT (+X)
            0.5, 0.5, 0.5, 1.0, 0.0, 0.0, 1.0, 0.0,
            0.5, 0.5, -0.5, 1.0, 0.0, 0.0, 1.0, 1.0,
            0.5, -0.5, -0.5, 1.0, 0.0, 0.0, 0.0, 1.0,
            0.5, -0.5, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0,

            # BOTTOM (-Y)
            -0.5, -0.5, -0.5, 0.0, -1.0, 0.0, 0.0, 1.0,
            0.5, -0.5, -0.5, 0.0, -1.0, 0.0, 1.0, 1.0,
            0.5, -0.5, 0.5, 0.0, -1.0, 0.0, 1.0, 0.0,
            -0.5, -0.5, 0.5, 0.0, -1.0, 0.0, 0.0, 0.0,

            # TOP (+Y)
            -0.5, 0.5, -0.5, 0.0, 1.0, 0.0, 0.0, 1.0,
            0.5, 0.5, -0.5, 0.0, 1.0, 0.0, 1.0, 1.0,
            0.5, 0.5, 0.5, 0.0, 1.0, 0.0, 1.0, 0.0,
            -0.5, 0.5, 0.5, 0.0, 1.0, 0.0, 0.0, 0.0,
        ], dtype = np.float32)

        self.indices = np.array([
            0, 1, 2, 2, 3, 0,
            5, 4, 7, 7, 6, 5,
            8, 9, 10, 10, 11, 8,
            13, 12, 15, 15, 14, 13,
            16, 17, 18, 18, 19, 16,
            21, 20, 23, 23, 22, 21
        ], dtype = np.int32)

        self.vao, self.vbo, self.ebo = 0, 0, 0

        self.texture = Texture(tex_path)

    def start(self):
        self.vao = glGenVertexArrays(1)
        self.vbo = glGenBuffers(1)
        self.ebo = glGenBuffers(1)

        glBindVertexArray(self.vao)

        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.indices.nbytes, self.indices, GL_STATIC_DRAW)

        stride = 8 * self.vertices.itemsize

        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(3 * self.vertices.itemsize))
        glEnableVertexAttribArray(1)

        glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(6 * self.vertices.itemsize))
        glEnableVertexAttribArray(2)

        glBindVertexArray(0)

        self.texture.start()