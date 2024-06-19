from django.urls import path
from . import views

urlpatterns = [
    path('app53/', views.factorial_view, name='app53'),
]
