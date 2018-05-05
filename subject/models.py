from django.db import models

# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Chapter(models.Model):
    title = models.CharField(max_length=40)
    subject = models.ForeignKey(Subject, related_name='subject', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title
