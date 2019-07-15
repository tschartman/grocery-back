from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from visits import views

urlpatterns = [
    path('visits/', views.VisitList.as_view()),
    path('visits/<int:pk>/', views.VisitDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
