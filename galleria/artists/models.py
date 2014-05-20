from django.db import models
from model_utils.models import TimeStampedModel

from contacts.models import Contact

# Artist is a special version of contact
class Artist(TimeStampedModel):
    contact = models.OneToOneField(Contact, primary_key=True)

    biography = models.TextField()
    price = models.TextField()
    info = models.TextField()
    commission = models.TextField()

    def __str__(self):
        return("{} {} ".format(self.contact.name_first,self.contact.name_last))


