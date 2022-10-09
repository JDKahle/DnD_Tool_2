from django.urls import path
from .views import PersonHomeView

from . import views

urlpatterns = [
    #path('', views.simple_view),
    path('', PersonHomeView.as_view(), name='home'),
]