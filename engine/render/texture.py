from OpenGL.GL import *
from PIL import Image
import numpy as np

class Texture:
    def __init__(self, path, tex_id):
        self.path = path
        self.tex_id = tex_id
        # self.color = (color[0] * 255, color[1] * 255, color[2] * 255, 255)
    #
    # def start(self):
    #     self.tex_id = glGenTextures(1)
    #     glBindTexture(GL_TEXTURE_2D, self.tex_id)
    #
    #     glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    #     glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    #     glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    #     glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    #
    #     if self.path:
    #         image = Image.open(self.path)
    #         image = image.transpose(Image.FLIP_TOP_BOTTOM)  # Flip for OpenGL coordinates
    #         data = image.convert("RGBA").tobytes()
    #         width, height = image.size
    #     else:
    #         width, height = 1, 1
    #         # r, g, b, a = self.color
    #         r, g, b, a = (255, 255, 255, 255)
    #         color_texture = np.zeros((height, width, 4), dtype=np.uint8)
    #         color_texture[0, 0] = [r, g, b, a]
    #         data = color_texture.tobytes()
    #
    #     glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0,
    #                  GL_RGBA, GL_UNSIGNED_BYTE, data)
    #
    # def bind(self):
    #     glBindTexture(GL_TEXTURE_2D, self.tex_id)
    #
    # def unbind(self):
    #     glBindTexture(GL_TEXTURE_2D, 0)