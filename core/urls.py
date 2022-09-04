from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('visualizer/', include('visualizer.urls')),
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home')
]
