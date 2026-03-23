
import glfw
import numpy as np

class MouseListener:
    instance = None

    def __init__(self):
        if hasattr(self, "_initialized"):
            return

        self._initialized = True
        self.scrollX, self.scrollY = 0.0, 0.0
        self.mouseX, self.mouseY = 0.0, 0.0
        self.lastX, self.lastY = 0.0, 0.0
        self.mouse_button_pressed = np.zeros([3], dtype=bool)
        self.is_dragging = False

        # print(self.mouse_button_pressed)

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance

    def mouse_pos_callback(self, window, x_pos, y_pos):
        self.lastX = self.mouseX
        self.lastY = self.mouseY
        self.mouseX = x_pos
        self.mouseY = y_pos

    def mouse_button_callback(self, window, button, action, mods):
        if action == glfw.PRESS:
            if button < len(self.mouse_button_pressed):
                self.mouse_button_pressed[button] = True
        elif action == glfw.RELEASE:
            if button < len(self.mouse_button_pressed):
                self.mouse_button_pressed[button] = False

    def mouse_scroll_callback(self, window, x_offset, y_offset):
        self.scrollX = x_offset
        self.scrollY = y_offset

    def getX(self):
        return self.mouseX

    def getY(self):
        return self.mouseY

    def getDX(self):
        return self.lastX - self.mouseX

    def getDY(self):
        return self.lastY - self.mouseY

    def mouse_button_down(self, button):
        if button < len(self.mouse_button_pressed):
            return self.mouse_button_pressed[button]
        return False