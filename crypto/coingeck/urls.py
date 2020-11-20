from django.urls import path

from . import views

urlpatterns = [
    path('tabet/',views.tabet,name = 'tablet')
]