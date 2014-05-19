# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Contact.reference'
        db.alter_column('contacts_contact', 'reference', self.gf('django.db.models.fields.CharField')(max_length=255))

    def backwards(self, orm):

        # Changing field 'Contact.reference'
        db.alter_column('contacts_contact', 'reference', self.gf('django.db.models.fields.CharField')(max_length=100))

    models = {
        'categories.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'contacts.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts.Contact']"}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'contacts.contact': {
            'Meta': {'object_name': 'Contact'},
            'addressed_as': ('django.db.models.fields.CharField', [], {'max_length': '100', 'default': "'calculated'"}),
            'addressed_as_custom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "''", 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['categories.Category']", 'symmetrical': 'False'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '100', 'default': "''", 'blank': 'True'}),
            'company_or_individual': ('django.db.models.fields.CharField', [], {'max_length': '10', 'default': "'individual'"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '100', 'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'default': "''", 'blank': 'True'}),
            'main_address': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['contacts.Address']", 'related_name': "'main_address'", 'blank': 'True'}),
            'main_phonenumber': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['contacts.PhoneNumber']", 'related_name': "'main_phonenumber'", 'blank': 'True'}),
            'migration_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name_first': ('django.db.models.fields.CharField', [], {'max_length': '100', 'default': "''", 'blank': 'True'}),
            'name_last': ('django.db.models.fields.CharField', [], {'max_length': '100', 'default': "''", 'blank': 'True'}),
            'name_middle': ('django.db.models.fields.CharField', [], {'max_length': '100', 'default': "''", 'blank': 'True'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "''", 'blank': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '100', 'default': "''", 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'default': "''", 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts.ContactType']"})
        },
        'contacts.contacts': {
            'Meta': {'object_name': 'contacts'},
            'address_business_1': ('django.db.models.fields.TextField', [], {}),
            'address_business_city': ('django.db.models.fields.TextField', [], {}),
            'address_business_country': ('django.db.models.fields.TextField', [], {}),
            'address_business_country_include': ('django.db.models.fields.TextField', [], {}),
            'address_business_county_state': ('django.db.models.fields.TextField', [], {}),
            'address_business_post_code': ('django.db.models.fields.TextField', [], {}),
            'address_city_selected': ('django.db.models.fields.TextField', [], {}),
            'address_company_include': ('django.db.models.fields.TextField', [], {}),
            'address_display_c1': ('django.db.models.fields.TextField', [], {}),
            'address_display_c1_line': ('django.db.models.fields.TextField', [], {}),
            'address_home_1': ('django.db.models.fields.TextField', [], {}),
            'address_home_city': ('django.db.models.fields.TextField', [], {}),
            'address_home_country': ('django.db.models.fields.TextField', [], {}),
            'address_home_country_include': ('django.db.models.fields.TextField', [], {}),
            'address_home_county_state': ('django.db.models.fields.TextField', [], {}),
            'address_home_post_code': ('django.db.models.fields.TextField', [], {}),
            'address_mail_override': ('django.db.models.fields.TextField', [], {}),
            'address_main': ('django.db.models.fields.TextField', [], {}),
            'address_map_c': ('django.db.models.fields.TextField', [], {}),
            'address_only_c': ('django.db.models.fields.TextField', [], {}),
            'address_only_line_c': ('django.db.models.fields.TextField', [], {}),
            'address_other_1': ('django.db.models.fields.TextField', [], {}),
            'address_other_city': ('django.db.models.fields.TextField', [], {}),
            'address_other_country': ('django.db.models.fields.TextField', [], {}),
            'address_other_country_include': ('django.db.models.fields.TextField', [], {}),
            'address_other_county_state': ('django.db.models.fields.TextField', [], {}),
            'address_other_postcode': ('django.db.models.fields.TextField', [], {}),
            'address_selected': ('django.db.models.fields.FloatField', [], {}),
            'c__portal_filter_child': ('django.db.models.fields.TextField', [], {}),
            'categories': ('django.db.models.fields.TextField', [], {}),
            'categories_one_line': ('django.db.models.fields.TextField', [], {}),
            'cats_count': ('django.db.models.fields.FloatField', [], {}),
            'company': ('django.db.models.fields.TextField', [], {}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'creationtimestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'creationuseraccountname': ('django.db.models.fields.TextField', [], {}),
            'creationusername': ('django.db.models.fields.TextField', [], {}),
            'currentrecordnumber': ('django.db.models.fields.FloatField', [], {}),
            'display_address_email': ('django.db.models.fields.TextField', [], {}),
            'display_address_email_checkbox': ('django.db.models.fields.TextField', [], {}),
            'display_client': ('django.db.models.fields.TextField', [], {}),
            'email_1': ('django.db.models.fields.TextField', [], {}),
            'email_1_display': ('django.db.models.fields.TextField', [], {}),
            'email_1_type': ('django.db.models.fields.TextField', [], {}),
            'email_1_validation': ('django.db.models.fields.FloatField', [], {}),
            'email_2': ('django.db.models.fields.TextField', [], {}),
            'email_2_display': ('django.db.models.fields.TextField', [], {}),
            'email_2_type': ('django.db.models.fields.TextField', [], {}),
            'email_3': ('django.db.models.fields.TextField', [], {}),
            'email_3_display': ('django.db.models.fields.TextField', [], {}),
            'fax_main_c': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier_company': ('django.db.models.fields.FloatField', [], {}),
            'identifier_individual': ('django.db.models.fields.FloatField', [], {}),
            'job_title': ('django.db.models.fields.TextField', [], {}),
            'job_title_include': ('django.db.models.fields.TextField', [], {}),
            'kf__categories': ('django.db.models.fields.TextField', [], {}),
            'kf__outlook_contacts_folder': ('django.db.models.fields.FloatField', [], {}),
            'kp__contacts': ('django.db.models.fields.FloatField', [], {}),
            'marketingemailtempinclude': ('django.db.models.fields.FloatField', [], {}),
            'marketingincludeemail': ('django.db.models.fields.FloatField', [], {}),
            'marketingincludemail': ('django.db.models.fields.FloatField', [], {}),
            'marketingposttempinclude': ('django.db.models.fields.FloatField', [], {}),
            'modificationtimestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'modificationuser': ('django.db.models.fields.TextField', [], {}),
            'modificationuseraccountname': ('django.db.models.fields.TextField', [], {}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name_addressed_as': ('django.db.models.fields.TextField', [], {}),
            'name_addressed_as_select': ('django.db.models.fields.TextField', [], {}),
            'name_first': ('django.db.models.fields.TextField', [], {}),
            'name_full_c': ('django.db.models.fields.TextField', [], {}),
            'name_last': ('django.db.models.fields.TextField', [], {}),
            'name_middle': ('django.db.models.fields.TextField', [], {}),
            'name_middle_include': ('django.db.models.fields.TextField', [], {}),
            'name_suffix': ('django.db.models.fields.TextField', [], {}),
            'name_suffix_include': ('django.db.models.fields.TextField', [], {}),
            'name_title': ('django.db.models.fields.TextField', [], {}),
            'name_title_include': ('django.db.models.fields.TextField', [], {}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'outlook_contacts_folder': ('django.db.models.fields.TextField', [], {}),
            'outlook_id': ('django.db.models.fields.TextField', [], {}),
            'outlook_id_reversed': ('django.db.models.fields.TextField', [], {}),
            'outlook_modificationtimestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'phone_business_1': ('django.db.models.fields.TextField', [], {}),
            'phone_business_2': ('django.db.models.fields.TextField', [], {}),
            'phone_business_fax': ('django.db.models.fields.TextField', [], {}),
            'phone_home_1': ('django.db.models.fields.TextField', [], {}),
            'phone_home_2': ('django.db.models.fields.TextField', [], {}),
            'phone_home_fax': ('django.db.models.fields.TextField', [], {}),
            'phone_main_c': ('django.db.models.fields.TextField', [], {}),
            'phone_main_selector': ('django.db.models.fields.TextField', [], {}),
            'phone_mobile': ('django.db.models.fields.TextField', [], {}),
            'phone_other': ('django.db.models.fields.TextField', [], {}),
            'phone_other_fax': ('django.db.models.fields.TextField', [], {}),
            'portalfilterkeychild': ('django.db.models.fields.TextField', [], {}),
            'recorddisplay': ('django.db.models.fields.TextField', [], {}),
            'recordmodificationcount': ('django.db.models.fields.FloatField', [], {}),
            'referral_info': ('django.db.models.fields.TextField', [], {}),
            'salutationcalc': ('django.db.models.fields.TextField', [], {}),
            'salutationname': ('django.db.models.fields.TextField', [], {}),
            'salutationtype': ('django.db.models.fields.TextField', [], {}),
            'search_c': ('django.db.models.fields.TextField', [], {}),
            'search_field': ('django.db.models.fields.TextField', [], {}),
            'tab_hide_id': ('django.db.models.fields.FloatField', [], {}),
            'tab_title': ('django.db.models.fields.TextField', [], {}),
            'type': ('django.db.models.fields.TextField', [], {}),
            'type_trigger': ('django.db.models.fields.TextField', [], {}),
            'url': ('django.db.models.fields.TextField', [], {}),
            'vat_rate': ('django.db.models.fields.FloatField', [], {})
        },
        'contacts.contacttype': {
            'Meta': {'object_name': 'ContactType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'contacts.note': {
            'Meta': {'object_name': 'Note'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts.Contact']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'note': ('django.db.models.fields.TextField', [], {})
        },
        'contacts.phonenumber': {
            'Meta': {'object_name': 'PhoneNumber'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts.Contact']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['contacts']