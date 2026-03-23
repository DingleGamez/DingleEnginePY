import glfw
import numpy as np

class KeyListener:
    instance = None

    def __init__(self):
        if hasattr(self, "_initialized"):
            return

        self._initialized = True
        self.key_pressed = np.zeros([glfw.KEY_LAST], dtype=bool)

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance

    def key_callback(self, window, key, scancode, action, mods):
        # if key >= 0 and key <= len(self.key_pressed):
        if action == glfw.PRESS:
            self.key_pressed[key] = True
        elif action == glfw.RELEASE:
            self.key_pressed[key] = False

    def is_key_pressed(self, key):
        # if key >= 0 and key <= len(self.get().key_pressed):
        return self.key_pressed[key]
