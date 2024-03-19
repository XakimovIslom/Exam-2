from django.db import models


class Product(models.Model):
    price = models.DecimalField(max_digits=5, decimal_places=2)
    marja = models.DecimalField(max_digits=5, decimal_places=2)
    package_code = models.CharField(max_length=50)

    def __str__(self):
        return self.package_code
