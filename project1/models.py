from django.db import models

from common.models import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class Region(BaseModel):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class Company(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()

    image = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.title


class Vacancy(BaseModel):
    title = models.CharField(max_length=255, blank=True, null=True)

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="categories"
    )
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="vacancies"
    )

    description = models.TextField(blank=True, null=True)

    from_price = models.IntegerField(blank=True, null=True)
    to_price = models.IntegerField(blank=True, null=True)

    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    @property
    def calculated_price(self):
        average_price = (self.from_price + self.to_price) / 2
        if self.to_price / self.from_price > 2:
            return (self.from_price + average_price) / 2 - (average_price + self.to_price) / 2
        elif self.from_price / self.from_price < 2:
            return average_price


class JobSeekers(BaseModel):
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name="regions",
    )
    vacancy = models.ForeignKey(
        Vacancy, on_delete=models.CASCADE, related_name="vacancies"
    )

    first_name = models.CharField(max_length=256, blank=True, null=True)
    last_name = models.CharField(max_length=256, blank=True, null=True)
    job = models.CharField(max_length=256)

    avatar = models.ImageField(upload_to="jobseekers/")

    price = models.IntegerField()

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"
