from django.conf.urls import include, url
from django.urls import path
from . import views

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', views.UsersViewSet)
router.register(r'relations', views.RelationsViewSet)
urlpatterns = [ 
]
urlpatterns += router.urls


