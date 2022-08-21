from django.urls import path
from . import views

appname = 'visualizer'
urlpatterns = [
    path('', views.index, name='index'),
    path('classroom-registration/', views.classroom_registration, name='classroom-registration'),
    path('classroom-created/', views.classroom_created, name='classroom-created'),
    path('<str:class_id>/', views.classroom_overview, name='classroom'),
    path('<str:class_id>/grades', views.grades, name='grades'),
]
