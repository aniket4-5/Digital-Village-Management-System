from django.urls import path
from villageapp import views
urlpatterns = [
    path('',views.home, name="village-home" ),
]
