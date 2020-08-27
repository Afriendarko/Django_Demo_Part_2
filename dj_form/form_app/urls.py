from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('form', views.details, name='form'),
    path('emp_form', views.modform, name='modform_form'),
]