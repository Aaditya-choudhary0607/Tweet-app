from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('',views.tweetlist,name='Tweet list'),
    path('create/',views.tweetcreate,name='tweetcreate'),
    path('<int:tweetid>/edit/',views.tweetedit,name='tweetedit'),
    path('<int:tweetid>/delete/',views.tweetdelete,name='tweetdelete'),
    
]