from django.core.urlresolvers import reverse
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return("{}".format(self.name))

    def __repr__(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural = 'categories'


