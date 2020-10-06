from django.urls import path
from . import views

app_name = 'qiiteru'
urlpatterns = [
   path('', views.index, name='index'),
]
