from django.urls import path, include
from .api import views
from rest_framework import routers

api = routers.DefaultRouter()
api.register(r'organizations', views.OrganizationViewset, basename='organizations')

api_urls = (api.urls, 'api')

urlpatterns = [
    path('', include(api_urls)),
]
