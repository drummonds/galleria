# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Artist.gallery_id'
        db.add_column('artists_artist', 'gallery_id',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'Artist.commission'
        db.add_column('artists_artist', 'commission',
                      self.gf('django.db.models.fields.DecimalField')(blank=True, decimal_places=3, default=0.5, max_digits=4),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Artist.gallery_id'
        db.delete_column('artists_artist', 'gallery_id')

        # Deleting field 'Artist.commission'
        db.delete_column('artists_artist', 'commission')


    models = {
        'artists.artist': {
            'Meta': {'object_name': 'Artist'},
            'biography': ('django.db.models.fields.TextField', [], {}),
            'commission': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'decimal_places': '3', 'default': '0.5', 'max_digits': '4'}),
            'contact': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['contacts.Contact']", 'primary_key': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'gallery_id': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'price': ('django.db.models.fields.TextField', [], {})
        },
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
            'addressed_as_custom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True', 'default': "''"}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['categories.Category']", 'symmetrical': 'False', 'null': 'True'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'default': "''"}),
            'company_or_individual': ('django.db.models.fields.CharField', [], {'max_length': '10', 'default': "'individual'"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_artist': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'job_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'default': "''"}),
            'main_address': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['contacts.Address']", 'related_name': "'main_address'", 'null': 'True'}),
            'main_phonenumber': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['contacts.PhoneNumber']", 'related_name': "'main_phonenumber'", 'null': 'True'}),
            'migration_id': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name_first': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'default': "''"}),
            'name_last': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'default': "''"}),
            'name_middle': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'default': "''"}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True', 'default': "''"}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'default': "''"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'default': "''"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts.ContactType']"})
        },
        'contacts.contacttype': {
            'Meta': {'object_name': 'ContactType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'contacts.phonenumber': {
            'Meta': {'object_name': 'PhoneNumber'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts.Contact']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['artists']