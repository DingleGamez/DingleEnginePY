from PIL import Image
from OpenGL.GL import *
import numpy as np

class Texture:
    def __init__(self):
        self.path = ""
        self.tex_id = None

    def init(self, path):
        if path:
            self.path = path
            image = Image.open(self.path)
            image = image.transpose(Image.FLIP_TOP_BOTTOM)  # Flip for OpenGL coordinates
            data = image.convert("RGBA").tobytes()
            width, height = image.size
        else:
            width, height = 1, 1
            white_texture = np.ones((height, width, 4), dtype=np.uint8) * 255  # RGBA
            data = white_texture.tobytes()

        self.tex_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.tex_id)

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0,
                    GL_RGBA, GL_UNSIGNED_BYTE, data)

    def bind(self):
        glBindTexture(GL_TEXTURE_2D, self.tex_id)

    def unbind(self):
        glBindTexture(GL_TEXTURE_2D, 0)