#django/rest_framework imports.
from django.contrib import admin
from django.urls import include, path

# app Level imports.
from address import views as address_views

# third party imports.
from rest_framework.routers import SimpleRouter

# Intialize DefaultRouter.
router = SimpleRouter()

# register address app urls with router.
router.register(r'address', address_views.FileViewSet, base_name='address')


urlpatterns = [
    # path(r'admin/', admin.site.urls),
    path('api/v1/', include((router.urls, 'api'), namespace='v1')),
]
