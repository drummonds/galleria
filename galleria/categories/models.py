from django.db import models

class Category(models.Model):
	class Meta:
		verbose_name_plural = 'categories'

	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name