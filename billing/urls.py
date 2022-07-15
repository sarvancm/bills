from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('logout/',views.logout_request, name='logout' ),
    path('billing/', views.billing, name='billing'),
    path('billingselect/', views.billingselect, name='billingselect'),
    path('billpayment/', views.billpayment, name='billpayment'),
    path('billpaymentselect/', views.billpaymentselect, name='billpaymentselect'),
    path('billselect/', views.billselect, name='billselect'),
    path('calculate/', views.calculate, name='calculate'),
    path('view/<int:id>', views.view, name='view'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('adddatabase/', views.adddatabase, name='adddatabase'),
    path('searchbase/', views.searchbase, name='searchbase'),
    path('searchbase/search/', views.search, name='search'),
    path('notification/', views.notification, name='notification'),
    ]