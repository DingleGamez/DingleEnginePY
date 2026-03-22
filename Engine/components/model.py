from engine.components.component import Component
from engine.render.texture import Texture
from engine.render.mesh import Mesh

from pyassimp import load
from pyassimp.material import aiTextureType_DIFFUSE
import numpy as np
from OpenGL.GL import *
import os

class Model(Component):
    def __init__(self, mesh_path=None):
        super().__init__()

        # self.vertices = np.array([
        #     # FRONT (+Z)
        #     -0.5, -0.5, 0.5, 0.0, 0.0, 1.0, 0.0, 0.0,
        #     0.5, -0.5, 0.5, 0.0, 0.0, 1.0, 1.0, 0.0,
        #     0.5, 0.5, 0.5, 0.0, 0.0, 1.0, 1.0, 1.0,
        #     -0.5, 0.5, 0.5, 0.0, 0.0, 1.0, 0.0, 1.0,
        #
        #     # BACK (-Z)
        #     -0.5, -0.5, -0.5, 0.0, 0.0, -1.0, 1.0, 0.0,
        #     0.5, -0.5, -0.5, 0.0, 0.0, -1.0, 0.0, 0.0,
        #     0.5, 0.5, -0.5, 0.0, 0.0, -1.0, 0.0, 1.0,
        #     -0.5, 0.5, -0.5, 0.0, 0.0, -1.0, 1.0, 1.0,
        #
        #     # LEFT (-X)
        #     -0.5, 0.5, 0.5, -1.0, 0.0, 0.0, 1.0, 0.0,
        #     -0.5, 0.5, -0.5, -1.0, 0.0, 0.0, 1.0, 1.0,
        #     -0.5, -0.5, -0.5, -1.0, 0.0, 0.0, 0.0, 1.0,
        #     -0.5, -0.5, 0.5, -1.0, 0.0, 0.0, 0.0, 0.0,
        #
        #     # RIGHT (+X)
        #     0.5, 0.5, 0.5, 1.0, 0.0, 0.0, 1.0, 0.0,
        #     0.5, 0.5, -0.5, 1.0, 0.0, 0.0, 1.0, 1.0,
        #     0.5, -0.5, -0.5, 1.0, 0.0, 0.0, 0.0, 1.0,
        #     0.5, -0.5, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0,
        #
        #     # BOTTOM (-Y)
        #     -0.5, -0.5, -0.5, 0.0, -1.0, 0.0, 0.0, 1.0,
        #     0.5, -0.5, -0.5, 0.0, -1.0, 0.0, 1.0, 1.0,
        #     0.5, -0.5, 0.5, 0.0, -1.0, 0.0, 1.0, 0.0,
        #     -0.5, -0.5, 0.5, 0.0, -1.0, 0.0, 0.0, 0.0,
        #
        #     # TOP (+Y)
        #     -0.5, 0.5, -0.5, 0.0, 1.0, 0.0, 0.0, 1.0,
        #     0.5, 0.5, -0.5, 0.0, 1.0, 0.0, 1.0, 1.0,
        #     0.5, 0.5, 0.5, 0.0, 1.0, 0.0, 1.0, 0.0,
        #     -0.5, 0.5, 0.5, 0.0, 1.0, 0.0, 0.0, 0.0,
        # ], dtype = np.float32)

        # self.indices = np.array([
        #     0, 1, 2, 2, 3, 0,
        #     5, 4, 7, 7, 6, 5,
        #     8, 9, 10, 10, 11, 8,
        #     13, 12, 15, 15, 14, 13,
        #     16, 17, 18, 18, 19, 16,
        #     21, 20, 23, 23, 22, 21
        # ], dtype = np.int32)

        self.meshes = np.array([], dtype=Mesh)
        self.mesh_path = mesh_path

        self.load_model(mesh_path)

    def load_model(self, model_path):
        with load(model_path) as scene:
            self.process_scene(scene)

    def process_scene(self, aiscene):
        for i in range(len(aiscene.meshes)):
            self.meshes = np.append(self.meshes, self.process_mesh(aiscene.meshes[i], aiscene))

    def process_mesh(self, aimesh, aiscene):
        vertices = np.array(aimesh.vertices, dtype=np.float32)
        indices = np.array([i for face in aimesh.faces for i in face], dtype=np.int32)
        normals = np.array(aimesh.normals, dtype=np.float32)
        texcoords = np.array(aimesh.texturecoords[0][:, :2], dtype=np.float32)

        material = aiscene.materials[aimesh.materialindex]
        color = material.properties.get(('diffuse', 0), [1,1,1])

        mesh = Mesh(vertices, indices, normals, texcoords, color)
        return mesh

    def draw(self, shader):
        for i in range(len(self.meshes)):
            self.meshes[i].draw(shader)

    # def start(self):
    #