from django.urls import path
from project1 import views

urlpatterns = [
    path("", views.VacancyCompanyResumeListApiView.as_view()),
    path("vacancy/", views.VacancyListAPIView.as_view()),
]
