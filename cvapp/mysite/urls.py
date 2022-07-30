from django.urls import path
from. import views


urlpatterns = [
    path('',views.index),
    path('',views.advert_new),
    path('', views.list_view)
  
]


