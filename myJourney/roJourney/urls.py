from django.urls import path
from . import views

app_name = 'roJourney'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_me, name='aboutMe'),
]
