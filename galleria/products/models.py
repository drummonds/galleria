from django.core.urlresolvers import reverse
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    COLOUR_CHOICES = (
        ('NR', 'Navy/Red'),
        ('NB', 'Navy/Blue'),
        ('GR', 'Green/Red'),
        ('GB', 'Green/Blue'),
    )
    has_colour = models.BooleanField()
    colour = models.CharField(max_length=2, choices=COLOUR_CHOICES)
    has_size = models.BooleanField()
    size = models.DecimalField(max_digits=5, decimal_places=2,blank=True)
    stock_quantity = models.IntegerField(default=0)
    item_price = models.DecimalField(max_digits=6, decimal_places=2)
    initials_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        if self.has_colour and self.has_size:
            return('{} {} {}"'.format(self.name,self.get_colour_display(),self.size))
        elif (not self.has_colour) and self.has_size:
            return('{} {}"'.format(self.name,self.size))
        elif self.has_colour and not self.has_size:
            return('{} {}'.format(self.name,self.get_colour_display()))
        else:
            return('{}'.format(self.name))

    def _get_description(self):
        "Returns a short description of the product."
        return('{}'.format(self.__str__()))
    description = property(_get_description)


    def __repr__(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])
