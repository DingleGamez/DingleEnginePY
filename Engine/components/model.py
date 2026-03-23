from engine.components.component import Component
from engine.render.texture import Texture
from engine.render.mesh import Mesh

from pyassimp import load
from pyassimp.material import aiTextureType_DIFFUSE
from PIL import Image
import numpy as np
from OpenGL.GL import *
import os

class Model(Component):
    def __init__(self, mesh_path=None):
        super().__init__()

        self.meshes = np.array([], dtype=Mesh)
        self.directory = os.path.dirname(mesh_path)
        self.loaded_textures = {}

        self.load_model(mesh_path)

    def load_model(self, model_path):
        with load(model_path) as scene:
            self.process_scene(scene)

    def process_scene(self, aiscene):
        for i in range(len(aiscene.meshes)):
            mesh = self.process_mesh(aiscene.meshes[i], aiscene)
            self.meshes = np.append(self.meshes, mesh)

    def process_mesh(self, aimesh, aiscene):
        vertices = np.array(aimesh.vertices, dtype=np.float32)
        indices = np.array([i for face in aimesh.faces for i in face], dtype=np.int32)
        normals = np.array(aimesh.normals, dtype=np.float32)

        if hasattr(aimesh, "texturecoords") and aimesh.texturecoords is not None and len(aimesh.texturecoords) > 0:
            texcoords = np.array(aimesh.texturecoords[0][:, :2], dtype=np.float32)
        else:
            texcoords = np.zeros((len(vertices), 2), dtype=np.float32)

        material = aiscene.materials[aimesh.materialindex]
        textures = self.load_textures(material)
        color = self.load_color(material)
        # textures = np.array([])

        # print(textures)

        mesh = Mesh(vertices, indices, normals, texcoords, textures, color)
        return mesh

    def load_color(self, material):
        diffuse = np.array([1.0, 1.0, 1.0], dtype=np.float32)

        for key, value in material.properties.items():
            if not isinstance(value, (list, tuple, np.ndarray)):
                continue

            print(key, value)

            key_lower = key.lower()

            if "diffuse" in key_lower:
                print(value)
                diffuse = np.array(value[:3], dtype=np.float32)

        return diffuse

    def load_textures(self, material):
        textures = np.array([], dtype=Texture)

        # print(material.properties)

        for key, value in material.properties.items():
            if not isinstance(value, str):
                continue

            # path = value[3:]

            full_path = os.path.normpath(os.path.join(self.directory, value))

            key_lower = key.lower()

            # print(key_lower)

            if "file" in key_lower or "map_kd" in key_lower:
                texture = self.load_texture_cached(full_path)
                if texture:
                    textures = np.append(textures, texture)

        return textures

    def load_texture_cached(self, path):
        if path in self.loaded_textures:
            return self.loaded_textures[path]

        if not os.path.exists(path):
            print("Missing texture:", path)
            return None

        img = Image.open(path).convert("RGBA")
        # img = img.transpose(Image.FLIP_TOP_BOTTOM)
        img_data = np.array(img, dtype=np.uint8)

        tex_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, tex_id)

        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img.width, img.height, 0,
                     GL_RGBA, GL_UNSIGNED_BYTE, img_data)

        glGenerateMipmap(GL_TEXTURE_2D)

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        glBindTexture(GL_TEXTURE_2D, 0)

        texture = Texture(path, tex_id)
        self.loaded_textures[path] = texture
        return texture

    def draw(self, shader):
        for i in range(len(self.meshes)):
            self.meshes[i].draw(shader)