from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

