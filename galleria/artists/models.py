from django.core.urlresolvers import reverse
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

    def _get_id(self):
        "Returns the primary key which is contact_id in this case."
        result=self.contact.id
        return(result)
    id = property(_get_id)

    def __str__(self):
        return("{} {} {} ".format(self.contact.name_first,self.contact.name_last,str(self.gallery_id)))

    def __repr__(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse('artist_detail', args=[str(self.id)])
