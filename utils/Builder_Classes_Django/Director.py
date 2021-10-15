from BuilderClass import BuilderClass


class Director:

    builderClass:BuilderClass

    def __init__(self, builderClass:BuilderClass):
        self.builderClass=builderClass

    def builder(self)->None:
        self.builderClass.add_imports()
        self.builderClass.add_name_class()
        self.builderClass.add_attri(None)
        self.builderClass.add_method(None)
