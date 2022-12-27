
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('courses', views.CourseViewSet)
router.register('lessons', views.LessonViewSet)
router.register('users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]