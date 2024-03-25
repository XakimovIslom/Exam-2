from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics
from rest_framework.response import Response

from project1.models import JobSeekers, Vacancy
from project1.serializers import VacancySerializer


@method_decorator(cache_page(60 * 15), name="dispatch")
class VacancyCompanyResumeListApiView(generics.ListAPIView):
    serializer_class = VacancySerializer
    queryset = Vacancy.objects.all()

    def get(self, request, *args, **kwargs):
        vacancy_count = self.get_queryset().count()
        company_count = (
            Vacancy.objects.all().values("company__title").distinct().count()
        )
        resume_count = JobSeekers.objects.all().count()
        return Response(
            {
                "vacancy_count": vacancy_count,
                "company_count": company_count,
                "jobseekers_count": resume_count,
            }
        )


class VacancyListAPIView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
