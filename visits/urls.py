from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from visits import views

urlpatterns = [
    path('visits/', views.visit_list),
    path('visits/<int:pk>/', views.visit_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
