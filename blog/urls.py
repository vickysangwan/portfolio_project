from django.urls import path
from . import views

urlpatterns = [
    path('',views.allblog, name='allblog'),
    path('<int:blog_id>/',views.details, name='details'),
]