from django.urls import path
from . import views

appname = 'visualizer'
urlpatterns = [
    path('', views.index, name='index'),
    path('class-registration/', views.class_registration, name='class-registration'),
    path('classroom-created/', views.classroom_created, name='classroom-created'),
    path('<str:class_id>/', views.class_overview, name='class'),
    path('<str:class_id>/grades', views.grades, name='grades'),
]
