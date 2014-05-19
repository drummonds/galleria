from django.db import models
from model_utils.models import TimeStampedModel

from categories.models import Category

class Contact(TimeStampedModel):
    readonly_fields = ('migration_id',)

    type = models.ForeignKey('ContactType')
    title = models.CharField(max_length=100, blank=True, default='')
    name_first = models.CharField(max_length=100, blank=True, default='')
    name_middle = models.CharField(max_length=100, blank=True, default='')
    name_last  = models.CharField(max_length=100, blank=True, default='')
    suffix = models.CharField(max_length=100, blank=True, default='')
    addressed_as = models.CharField(max_length=100, choices=(('calculated','Calculated'),('custom','Custom'),), default='calculated')
    addressed_as_custom = models.CharField(max_length=255, blank=True, default='')
    categories = models.ManyToManyField(Category)
    reference = models.CharField(max_length=255, blank=True, default='')
    company_or_individual = models.CharField(verbose_name='client is', max_length=10, choices=(('company','company'),('individual','individual')), default='individual')
    company = models.CharField(max_length=100, blank=True, default='')
    job_title = models.CharField(max_length=100, blank=True, default='')
    department = models.CharField(max_length=100, blank=True, default='')

    main_phonenumber = models.ForeignKey('PhoneNumber', related_name='main_phonenumber', blank=True, null=True) # We may not have a phone number
    main_address = models.ForeignKey('Address', related_name='main_address', blank=True, null=True) # We may not have an address
    migration_id = models.IntegerField(blank=True, null=True)

    def _get_full_name(self):
        "Returns the person's full name."
        if self.name_middle:
            result='{} {} {}'.format(self.name_first, self.name_middle, self.name_last)
        else:
            result='{} {}'.format(self.name_first, self.name_last)
        return(result)
    full_name = property(_get_full_name)

    def _get_short_summary(self):
        "Returns a short summary of this contact."
        return('{}-{}'.format(self.full_name, self.type))
    short_summary = property(_get_short_summary)

    def __str__(self):
        return("{}".format(self.short_summary))

class PhoneNumber(models.Model):
    contact = models.ForeignKey(Contact)

    type = models.CharField(max_length=100)
    number = models.CharField(max_length=200)

class Address(models.Model):
    contact = models.ForeignKey(Contact)

    type = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    postcode = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class contacts(TimeStampedModel):
    address_city_selected    =models.TextField()
    address_display_c1    =models.TextField()
    address_display_c1_line    =models.TextField()
    address_map_c       =models.TextField()
    address_only_c      =models.TextField()
    address_only_line_c    =models.TextField()
    address_selected    =models.FloatField()
    c__portal_filter_child    =models.TextField()
    cats_count          =models.FloatField()
    display_address_email    =models.TextField()
    display_address_email_checkbox    =models.TextField()
    email_1_validation    =models.FloatField()
    fax_main_c          =models.TextField()
    identifier_company    =models.FloatField()
    identifier_individual    =models.FloatField()
    job_title           =models.TextField()
    kf__categories      =models.TextField()
    kf__outlook_contacts_folder    =models.FloatField()
    kp__contacts        =models.FloatField()
    marketingemailtempinclude    =models.FloatField()
    marketingincludeemail    =models.FloatField()
    marketingposttempinclude    =models.FloatField()
    name_addressed_as    =models.TextField()
    name_addressed_as_select    =models.TextField()
    name_full_c         =models.TextField()
    outlook_contacts_folder    =models.TextField()
    outlook_id          =models.TextField()
    outlook_id_reversed    =models.TextField()
    outlook_modificationtimestamp    =models.DateTimeField()
    phone_main_c        =models.TextField()
    portalfilterkeychild    =models.TextField()
    recorddisplay       =models.TextField()
    salutationcalc      =models.TextField()
    search_c            =models.TextField()
    search_field        =models.TextField()
    tab_hide_id         =models.FloatField()
    tab_title           =models.TextField()
    type_trigger        =models.TextField() #  address_info
    address_business_1    =models.TextField() #  address_info
    address_business_city    =models.TextField() #  address_info
    address_business_country    =models.TextField() #  address_info
    address_business_country_include    =models.TextField() #  address_info
    address_business_county_state    =models.TextField() #  address_info
    address_business_post_code    =models.TextField() #  address_info
    address_company_include    =models.TextField() #  address_info
    address_home_1      =models.TextField() #  address_info
    address_home_city    =models.TextField() #  address_info
    address_home_country    =models.TextField() #  address_info
    address_home_country_include    =models.TextField() #  address_info
    address_home_county_state    =models.TextField() #  address_info
    address_home_post_code    =models.TextField() #  address_info:: Manual override for address where logic doesnt work
    address_mail_override    =models.TextField() #  address_info:: Selector of Business, Home or Other
    address_main        =models.TextField() #  address_info
    address_other_1     =models.TextField() #  address_info
    address_other_city    =models.TextField() #  address_info
    address_other_country    =models.TextField() #  address_info
    address_other_country_include    =models.TextField() #  address_info
    address_other_county_state    =models.TextField() #  address_info
    address_other_postcode    =models.TextField() #  address_info
    company             =models.TextField() #  address_info:: ? this is how the client appears in a sorting list
    display_client      =models.TextField() #  address_info
    job_title_include    =models.TextField() #  address_info:: About 90% have a first name
    name_first          =models.TextField() #  address_info:: About 95% have a last name
    name_last           =models.TextField() #  address_info
    name_middle         =models.TextField() #  address_info
    name_middle_include    =models.TextField() #  address_info
    name_suffix         =models.TextField() #  address_info
    name_suffix_include    =models.TextField() #  address_info:: About half have a title
    name_title          =models.TextField() #  address_info:: ? include this title on a mailing list
    name_title_include    =models.TextField() #  address_info
    salutationname      =models.TextField() #  address_info
    salutationtype      =models.TextField() #  address_info
    url                 =models.TextField() #  categories
    categories          =models.TextField() #  categories
    categories_one_line    =models.TextField() #  categories
    type                =models.TextField() #  commercial
    referral_info       =models.TextField() #  commercial
    vat_rate            =models.FloatField() #  email_info
    email_1             =models.TextField() #  email_info
    email_1_display     =models.TextField() #  email_info
    email_1_type        =models.TextField() #  email_info
    email_2             =models.TextField() #  email_info
    email_2_display     =models.TextField() #  email_info
    email_2_type        =models.TextField() #  email_info
    email_3             =models.TextField() #  email_info
    email_3_display     =models.TextField() #  marketing_info
    marketingincludemail    =models.FloatField() #  modification_log
    creationtimestamp    =models.DateTimeField() #  modification_log
    creationuseraccountname    =models.TextField() #  modification_log
    creationusername    =models.TextField() #  modification_log
    modificationtimestamp    =models.DateTimeField() #  modification_log
    modificationuser    =models.TextField() #  modification_log
    modificationuseraccountname    =models.TextField() #  modification_log
    recordmodificationcount    =models.FloatField() #  notes
    notes               =models.TextField() #  phone_info
    phone_business_1    =models.TextField() #  phone_info
    phone_business_2    =models.TextField() #  phone_info
    phone_business_fax    =models.TextField() #  phone_info
    phone_home_1        =models.TextField() #  phone_info
    phone_home_2        =models.TextField() #  phone_info
    phone_home_fax      =models.TextField() #  phone_info
    phone_main_selector    =models.TextField() #  phone_info
    phone_mobile        =models.TextField() #  phone_info
    phone_other         =models.TextField() #  phone_info
    phone_other_fax     =models.TextField() #  row_id
    currentrecordnumber    =models.FloatField() # row_id

class Note(TimeStampedModel):
    contact = models.ForeignKey(Contact)
    note = models.TextField()

class ContactType(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return("{}".format(self.name))

