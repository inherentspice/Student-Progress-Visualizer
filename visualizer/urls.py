from django.urls import path
from . import views

app_name = 'visualizer'
urlpatterns = [
    path('', views.index, name='index'),
    path('classroom-registration/', views.classroom_registration, name='classroom-registration'),
    path('<int:classroom_id>/', views.classroom_overview, name='classroom'),
    path('<int:classroom_id>/<int:student_id>/grades/', views.grades, name='grades'),
    path('<int:classroom_id>/<int:student_id>/student-update', views.student_update, name='student-update'),
    path('<int:classroom_id>/<int:student_id>/student-delete', views.student_delete, name='student-delete'),
    path('<int:classroom_id>/classroom-update', views.classroom_update, name='classroom-update'),
    path('<int:classroom_id>/classroom-delete', views.classroom_delete, name='classroom-delete'),
    path('<int:classroom_id>/<int:student_id>/chart/', views.charts, name='charts'),
    path('<int:student_id>/grades-chart/', views.grades_chart, name='grades-chart'),

]
