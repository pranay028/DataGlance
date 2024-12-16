from django.urls import path
from . import views

urlpatterns = [
    path('generate-report/', views.generate_report, name='generate_report'),
    path('update-column-name/', views.update_column, name='update_column'),
    
]