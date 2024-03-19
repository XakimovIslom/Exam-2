from django.db import models


class Vacancy(models.Model):
    salary_from = models.DecimalField(max_digits=10, decimal_places=2)
    salary_to = models.DecimalField(max_digits=10, decimal_places=2)
    salary = models.CharField(max_length=20)

    def __str__(self):
        return f"${self.salary_from} - ${self.salary_to} ({self.salary})"

    @classmethod
    def filter_by_salary(cls, amount):
        return cls.objects.filter(
            salary_from__gte=amount,
            salary_to__lte=amount,
        )
