from django.core.urlresolvers import reverse
from django.db import models

from model_utils.models import TimeStampedModel

from contacts.models import Contact,Address

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


class Order(TimeStampedModel):
    reference = models.CharField(max_length=255)
    delivery_note = models.CharField(max_length=255)
    comment = models.CharField(max_length=255, blank=True,default='')
    comment = models.CharField(max_length=255, blank=True,default='')
    ORDER_STATES = (
        ('EN', 'Entered'),
        ('PR', 'Processed'),
        ('DI', 'Dispatched'),
        ('CA', 'Cancelled'),
        ('RE', 'Returned'),
    )
    state = models.CharField(max_length=2, choices=ORDER_STATES)
    contact = models.ForeignKey(Contact)
    invoice_address = models.ForeignKey(Address, related_name="invoices", null=True, default=None)
    delivery_address = models.ForeignKey(Address, default=None, blank=True, related_name="deliveries", null=True)

    def __str__(self):
        return '{} {} ({})'.format(self.reference, self.contact, self.id )

    def _get_description(self):
        "Returns a short description of the product."
        return('{}'.format(self.__str__()))
    description = property(_get_description)


    def __repr__(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse('order_detail', args=[str(self.id)])


class OrderItem(models.Model):
    product = models.ForeignKey('Product')
    order = models.ForeignKey('Order')
    initial = models.CharField(max_length=50,blank=True)
    qty = models.IntegerField(default=1)
    item_price = models.DecimalField(max_digits=6, decimal_places=2)

    def _get_total_price(self):
        "Returns a short description of the product."
        return(self.qty*self.item_price)
    total_price = property(_get_total_price)
