from django.db import models

from model_utils.models import TimeStampedModel

from contacts.models import Contact


# Artist is a special version of contact
class Artist(TimeStampedModel):
    contact = models.OneToOneField(Contact, primary_key=True, limit_choices_to={'is_artist': True})

    gallery_id = models.IntegerField(blank=True,null=True)
    biography = models.TextField()
    price = models.TextField()
    info = models.TextField(blank=True)
    commission = models.DecimalField(max_digits=4, decimal_places=3,blank=True,default=0.5)

    def __str__(self):
        return("{} {} {} ".format(self.contact.name_first,self.contact.name_last,self.gallery_id))


