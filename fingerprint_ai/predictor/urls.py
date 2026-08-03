from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.upload, name='upload'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path(
        'download/<str:name>/<str:dob>/<str:mobile>/<str:result>/<str:confidence>/',
        views.download_report,
        name='download_report'
    ),

    path('patient/<int:id>/', views.patient_detail, name='patient_detail'),
    path('delete/<int:id>/', views.delete_prediction, name='delete_prediction'),
    

]