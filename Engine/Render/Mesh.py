import numpy
from OpenGL.GL import *
import numpy as np

class Mesh:
    def __init__(self):

        self.vertices = np.array([
            -0.5, -0.5, 0.5, 0.0, 0.0,
            0.5, -0.5, 0.5, 1.0, 0.0,
            0.5, 0.5, 0.5, 1.0, 1.0,
            -0.5, 0.5, 0.5, 0.0, 1.0,

            # BACK (-Z)
            -0.5, -0.5, -0.5, 1.0, 0.0,
            0.5, -0.5, -0.5, 0.0, 0.0,
            0.5, 0.5, -0.5, 0.0, 1.0,
            -0.5, 0.5, -0.5, 1.0, 1.0,

            # LEFT (-X)
            -0.5, 0.5, 0.5, 1.0, 0.0,
            -0.5, 0.5, -0.5, 1.0, 1.0,
            -0.5, -0.5, -0.5, 0.0, 1.0,
            -0.5, -0.5, 0.5, 0.0, 0.0,

            # RIGHT (+X)
            0.5, 0.5, 0.5, 1.0, 0.0,
            0.5, 0.5, -0.5, 1.0, 1.0,
            0.5, -0.5, -0.5, 0.0, 1.0,
            0.5, -0.5, 0.5, 0.0, 0.0,

            # BOTTOM (-Y)
            -0.5, -0.5, -0.5, 0.0, 1.0,
            0.5, -0.5, -0.5, 1.0, 1.0,
            0.5, -0.5, 0.5, 1.0, 0.0,
            -0.5, -0.5, 0.5, 0.0, 0.0,

            # TOP (+Y)
            -0.5, 0.5, -0.5, 0.0, 1.0,
            0.5, 0.5, -0.5, 1.0, 1.0,
            0.5, 0.5, 0.5, 1.0, 0.0,
            -0.5, 0.5, 0.5, 0.0, 0.0
        ], dtype=np.float32)

        self.indices = np.array([
            0, 1, 2, 2, 3, 0,  # front (+Z)

            5, 4, 7, 7, 6, 5,  # back (-Z) ✅ flipped

            8, 9, 10, 10, 11, 8,  # left (-X)

            13, 12, 15, 15, 14, 13,  # right (+X) ✅ flipped

            16, 17, 18, 18, 19, 16,  # bottom (-Y)

            21, 20, 23, 23, 22, 21  # top (+Y) ✅ flipped
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