from django.urls import path

from transport import views

app_name = 'transport'
urlpatterns = [
    path('', views.index, name='index'),
]
