from django.contrib import admin

from project1.models import Category, Company, JobSeekers, Region, Vacancy

admin.site.register(Category)
admin.site.register(Region)
admin.site.register(Company)
admin.site.register(Vacancy)
admin.site.register(JobSeekers)
