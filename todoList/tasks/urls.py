from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, index_view # Tambah index_view di sini

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', index_view, name='todo-ui'), 
    path('api/', include(router.urls)),   # Backend API
]