from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return("{}".format(self.name))

    class Meta:
        verbose_name_plural = 'categories'


