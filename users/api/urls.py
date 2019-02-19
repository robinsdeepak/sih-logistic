from django.urls import path, include
from rest_framework import routers
from users.api import views

router = routers.DefaultRouter()
router.register('', views.UserView)

urlpatterns = [
    path('', include(router.urls))
]
