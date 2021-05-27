from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('',TemplateView.as_view(template_name = 'index.html')),
    path('login/', views.Timetable, name = 'Timetable')
]
