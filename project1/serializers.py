from rest_framework import serializers

from project1.models import Company, JobSeekers, Vacancy


class VacancySerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(source='category.title')

    class Meta:
        model = Vacancy
        fields = ("category", "calculated_price")


