from django.core.urlresolvers import reverse
from django.db import models

class Stock(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return "%s" % (self.name)

	def __repr__(self):
		return self.__str__()

	def __unicode__(self):
		return u'%s' % (self.name)

	def get_absolute_url(self):
		return reverse('stock_detail', args=[str(self.id)])