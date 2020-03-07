from django.urls import path

from commerce import views

app_name = 'commerce'
urlpatterns = [
    path('', views.index, name='index'),
]
