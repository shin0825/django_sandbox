from django.urls import path
from . import views

app_name = 'qiiteru'
urlpatterns = [
   path('', views.index, name='index'),
   path('detail/<int:post_id>/', views.detail, name='detail'),
   path('add/', views.add, name='add'),
]
