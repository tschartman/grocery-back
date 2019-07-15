from django.urls import path
from visits import views

urlpatterns = [
    path('visits/', views.visit_list),
    path('visits/<int:pk>/', views.visit_detail),
]