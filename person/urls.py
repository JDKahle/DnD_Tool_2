from django.urls import path
from .views import PersonHomeView

from . import views

app_name = 'person'

urlpatterns = [
    #path('', views.simple_view),
    path('', PersonHomeView.as_view(), name='home'),
]