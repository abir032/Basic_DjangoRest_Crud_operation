from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    path('api', views.apiOverview, name='api'),
    path('apidtail/<int:pk>/', views.apidetail, name='apidetail'),
    path('admincreate', views.admincreate, name='admincreate'),
    path('adminupdate/<int:pk>/', views.adminupdate, name='adminupdate'),
    path('admindelete/<int:pk>/', views.admindelete, name='admindelte'),
] 
