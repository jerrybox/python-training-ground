from django.db import models


class Region(models.Model):
    GRADE_CHOICES = (
        ("province", 'Province'),
        ("city", 'City'),
        ("country", "Country"),
    )
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10, choices=GRADE_CHOICES,default="country")
