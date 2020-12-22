from django.urls import path

from . import views

app_name = 'wine_cellars'
urlpatterns = [
            # Main page
            path('', views.index, name='index'),
            # All bottles
            path('bottles/', views.bottles, name='bottles'),
            # Full info on one bottle
            path('bottles/<int:bottle_id>/', views.bottle, name ='bottle')
]
