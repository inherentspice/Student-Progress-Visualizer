from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:class_id>/', views.class_overview, name='class'),
    path('<str:class_id>/grades', views.grades, name='grades'),
]
