from django.urls import path
from . import views
urlpatterns =[
    path('',views.Test.as_view(),name='test'),
    path('signup',views.Signup.as_view(),name='signup'),
    path('usershow',views.Usershow.as_view(),name='usershow'),
    path('regapp',views.Regapp.as_view(),name='regapp'),
    path('applications',views.Applications.as_view(),name='applications'),
    path('slots',views.Slotsview.as_view(),name='slots'),
    path('checkemail',views.Checkemail.as_view(),name='checkemails'),
    path('userappsview',views.Userappview.as_view(), name='userappsview'),
    path('Checkusernewapp',views.Checkusernewapp.as_view(),name='checkusernewapp'),
    path('newapplicationslist',views.Newapplicationslist.as_view(),name='newapplicationslist'),
    path('approveapp/<int:pk>',views.Approveapp.as_view(),name='approveapp'),
    path('denyapp/<int:pk>',views.Denyapp.as_view(),name='denyapp'),
    path('getapprovedapps',views.Getapprovedapps.as_view(),name='getapprovedapps'),
    path('getdeniedapps', views.Getdeniedapps.as_view(), name='getdeniedapps'),
    path('getcompanyname/<int:pk>',views.GetCompanyname.as_view(),name='getcompanyname'),
    path('getapprovedcompanies',views.Getapprovedcompanies.as_view(),name='get'),
    path('assignslot/<int:pk>/<str:company_name>',views.Assignslot.as_view(),name='assignslot')


]