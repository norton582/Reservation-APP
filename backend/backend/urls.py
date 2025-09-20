
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from reservations.views import *

router = routers.DefaultRouter()
router.register(r'chambres', ChambreViewSet) 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
