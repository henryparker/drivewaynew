from django.urls import path

from . import views

app_name = 'userface'
urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('myvehicles/', views.VehicleListView.as_view(), name='my-vehicles'),
    path('register/', views.register, name='register'),
    path('search/', views.search, name='search'),
    path('registervehicle/',views.registervehicle, name = 'registervehicle'),
    path('addspot/',views.addspot, name = 'addspot'),
    path('search/results', views.search, name='search_results')
]