from django.urls import path
from . import views

urlpatterns = [
    path('aboutus/add/', views.AboutUsAdd.as_view(), name='about_us-add'),
    path('aboutus/<int:pk>/', views.AboutUsUpdate.as_view(), name='about_us-update'),
    path('aboutus/<int:pk>/', views.AboutUsDelete.as_view(), name='about_us-delete'),
]
