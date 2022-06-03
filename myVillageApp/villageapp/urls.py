from django.urls import path
from villageapp import views
urlpatterns = [
    path('', views.home, name="village-home"),
    path('about/', views.about, name="village-about"),
    path('notification/', views.notification, name="village-notification"),
    path('jobs/', views.jobs, name="village-jobs"),
    path('complaints/', views.complaints, name="village-complaints"),


]
