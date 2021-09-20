from django.urls import path, include
from rest_framework.routers import DefaultRouter
from task import views

router: DefaultRouter = DefaultRouter()
router.register('', views.SubTaskView, basename="")
urlpatterns = [
    path("", include(router.urls))
]
