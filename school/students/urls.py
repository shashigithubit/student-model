from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.student_detail, name='student_detail'),
]
