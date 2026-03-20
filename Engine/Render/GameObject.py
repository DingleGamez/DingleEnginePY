class GameObject:
    def __init__(self, name, transform):
        self.components = {}
        self.transform = transform
        self.name = name

    def addComponent(self, component):
        componentType = type(component)
        component.gameObject = self
        self.components[componentType] = component
        component.start()
        return component

    def getComponent(self, component_type):
        return self.components.get(component_type, None)

    def removeComponent(self, component_type):
        if component_type in self.components:
            del self.components[component_type]

    def updateComponents(self):
        for component in self.components.values():
            component.update()