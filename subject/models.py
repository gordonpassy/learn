from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('subject:subject_chapters', args=[self.id, self.slug])
