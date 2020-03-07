from django.urls import path

from settlement import views

app_name = 'settlement'
urlpatterns = [
    path('', views.index, name='index'),
]
