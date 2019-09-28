from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about-us'),
    path('blog', views.blog, name='blog'),
    path('consult', views.consult, name='consult'),
    path('admin1', views.admin1, name='admin'),


]
