from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from optparse import make_option

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--user',
            action='store',
            default=None,
            help='Username for new user'),
        make_option('--password',
            action='store',
            default=None,
            help='User password'),
        make_option('--email',
            action='store',
            default=None,
            help='User email address'),
        )

    def handle(self, *args, **kwargs):
        superuser = User.objects.create_superuser(
            username = kwargs.get('user'),
            email = kwargs.get('email'),
            password = kwargs.get('password')
            )
        superuser.save()
