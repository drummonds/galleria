from model_mommy import mommy
from contacts.models import Contact
from categories.models import Category
from django.conf import settings

settings.configure()

category = mommy.make(Categoy,3)
contact = mommy.make(Contact,3)
