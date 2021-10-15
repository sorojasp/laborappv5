from BuilderClass import BuilderClass


class BuilderUrls(BuilderClass):



    def __init__(self, appName: str, fields: list, nameFile: str):
        BuilderClass.__init__(self, appName, fields, nameFile)


    def add_imports(self):
        imports = f"""\
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from {self.appName} import views
"""
        self.fileUtil.writeToFile(self.nameFile, imports, True, True)

    def add_name_class(self):
        pass

    def add_attri(self, attri:list)->None:
        class_name = f"""\
router:DefaultRouter= DefaultRouter()
router.register('', views.{self.appName.capitalize()}Views, basename="")
urlpatterns=[
    path("", include(router.urls))
]

            """
        self.fileUtil.writeToFile(self.nameFile, class_name, True, True)

    def add_method(self, methods:str):
        pass
