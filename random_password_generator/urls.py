from django.urls import path
from . import views

urlpatterns = [

    path('',views.rpg, name="rpg"),
    path('about_us',views.about_us, name= 'about_us'),
    path('password',views.password, name= 'password'),

]
