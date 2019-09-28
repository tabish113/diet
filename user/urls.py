from django.urls import path
from . import views

urlpatterns=[
path('user-admin',views.index, name='user-login'),
path('user-contact1/<int:cid>',views.contact1, name='user-contact'),
path('user-contact',views.contact, name='user-contact'),

path('user-blog',views.blog, name='user-blog'),
path('edit-blog',views.editblog, name='user-blog'),
path('sign-Up',views.signup, name='signup'),



]
