from django.db import models


class ContactType(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __unicode__(self):
        return u"%s" % self.name