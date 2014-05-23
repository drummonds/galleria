# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Artist'
        db.create_table('artists_artist', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('contact', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['contacts.Contact'], primary_key=True, unique=True)),
            ('gallery_id', self.gf('django.db.models.fields.IntegerField')()),
            ('biography', self.gf('django.db.models.fields.TextField')()),
            ('price', self.gf('django.db.models.fields.TextField')()),
            ('info', self.gf('django.db.models.fields.TextField')()),
            ('commission', self.gf('django.db.models.fields.DecimalField')(decimal_places=3, max_digits=4)),
        ))
        db.send_create_signal('artists', ['Artist'])


    def backwards(self, orm):
        # Deleting model 'Artist'
        db.delete_table('artists_artist')


    models = {
        'artists.artist': {
            'Meta': {'object_name': 'Artist'},
            'biography': ('django.db.models.fields.TextField', [], {}),
            'commission': ('django.db.models.fields.DecimalField', [], {'decimal_places': '3', 'max_digits': '4'}),
            'contact': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['contacts.Contact']", 'primary_key': 'True', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'gallery_id': ('django.db.models.fields.IntegerField', [], {}),
            'info': ('django.db.models.fields.TextField', [], {}),
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
            'addressed_as': ('django.db.models.fields.CharField', [], {'default': "'calculated'", 'max_length': '100'}),
            'addressed_as_custom': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'null': 'True', 'blank': 'True', 'to': "orm['categories.Category']"}),
            'company': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'company_or_individual': ('django.db.models.fields.CharField', [], {'default': "'individual'", 'max_length': '10'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'department': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'main_address': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['contacts.Address']", 'blank': 'True', 'related_name': "'main_address'"}),
            'main_phonenumber': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['contacts.PhoneNumber']", 'blank': 'True', 'related_name': "'main_phonenumber'"}),
            'migration_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name_first': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'name_last': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'name_middle': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'reference': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
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
