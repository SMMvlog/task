from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('user1/',views.user1,name='user1'),
    path('user2/',views.user2,name='user2'),
    path('user3/',views.user3,name='user3'),
    path('sent/',views.sent,name='sent'),
]