from model_mommy import mommy
from contacts.models import Contact
from django.conf import settings

settings.configure()

contact = mommy.make(Contact,3)
