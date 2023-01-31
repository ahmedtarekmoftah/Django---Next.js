from django.db import models


class country(models.Model):
    name = models.CharField(max_length=64, default="Soon")
    title = models.CharField(max_length=64, default="Soon")
    flag = models.FileField(upload_to="main/images", null=True)
    anthem = models.FileField(upload_to="main/audio", null=True)
    name_ar = models.CharField(max_length=64, default="قريبا")
    title_ar = models.CharField(max_length=64, default="قريبا")
    capital = models.CharField(max_length=64, default="Soon")
    population = models.CharField(max_length=64, default="Soon")
    continent = models.CharField(max_length=64, default="Soon")
    area = models.CharField(max_length=64, default="Soon")
    religion = models.CharField(max_length=64, default="Soon")
    capital_ar = models.CharField(max_length=64, default="قريبا")
    continent_ar = models.CharField(max_length=64, default="قريبا")
    religion_ar = models.CharField(max_length=64, default="قريبا")
    location = models.CharField(max_length=1024, default="Soon")

    def __str__(self):
        return f"{self.id}. {self.name}"
