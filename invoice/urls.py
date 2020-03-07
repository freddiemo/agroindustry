from django.urls import path

from invoice import views

app_name = 'invoice'
urlpatterns = [
    path('', views.index, name='index'),
]
