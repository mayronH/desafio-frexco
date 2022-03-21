from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/json/', views.jsonUsers, name='json'),
    path('dashboard/csv/', views.csvUsers, name='csv'),
    path('dashboard/xlsx/', views.xlsxUsers, name='xlsx'),
]
