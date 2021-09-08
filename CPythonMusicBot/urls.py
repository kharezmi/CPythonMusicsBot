
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from botapp.views import UsersViewSet

router = routers.DefaultRouter()
router.register('Users', UsersViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    # path('api/', include('rest_framework.urls',  namespace='rest_framework')),
]

