import numpy
from OpenGL.GL import *
import numpy as np

class Mesh:
    def __init__(self):
        self.vertices = np.array([
            -0.5, -0.5, -0.5, 0.0, 0.0,  # 0
            0.5, -0.5, -0.5, 1.0, 0.0,  # 1
            0.5, 0.5, -0.5, 1.0, 1.0,  # 2
            -0.5, 0.5, -0.5, 0.0, 1.0,  # 3
            -0.5, -0.5, 0.5, 0.0, 0.0,  # 4
            0.5, -0.5, 0.5, 1.0, 0.0,  # 5
            0.5, 0.5, 0.5, 1.0, 1.0,  # 6
            -0.5, 0.5, 0.5, 0.0, 1.0,  # 7
        ], dtype=numpy.float32)

        self.indices = np.array([
            # back face
            0, 1, 2,
            2, 3, 0,
            # front face
            4, 5, 6,
            6, 7, 4,
            # left face
            0, 4, 7,
            7, 3, 0,
            # right face
            1, 5, 6,
            6, 2, 1,
            # bottom face
            0, 1, 5,
            5, 4, 0,
            # top face
            3, 2, 6,
            6, 7, 3,
        ], dtype=numpy.int32)

        self.VAO = glGenVertexArrays(1)
        self.VBO = glGenBuffers(1)
        self.EBO = glGenBuffers(1)

        self.setup()

    def setup(self):
        glBindVertexArray(self.VAO)

        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.EBO)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.indices.nbytes, self.indices, GL_STATIC_DRAW)

        stride = 5 * self.vertices.itemsize

        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(3 * self.vertices.itemsize))
        glEnableVertexAttribArray(1)

        glBindVertexArray(0)

    def draw(self):
        glBindVertexArray(self.VAO)

        glDrawElements(
            GL_TRIANGLES,
            len(self.indices),
            GL_UNSIGNED_INT,
            None
        )

        glBindVertexArray(0)