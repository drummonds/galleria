# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Order.comment'
        db.add_column('products_order', 'comment',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=255, default=''),
                      keep_default=False)

        # Adding field 'Order.invoice_address'
        db.add_column('products_order', 'invoice_address',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='invoices', null=True, to=orm['contacts.Address']),
                      keep_default=False)


        # Changing field 'Order.delivery_address'
        db.alter_column('products_order', 'delivery_address_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['contacts.Address']))

    def backwards(self, orm):
        # Deleting field 'Order.comment'
        db.delete_column('products_order', 'comment')

        # Deleting field 'Order.invoice_address'
        db.delete_column('products_order', 'invoice_address_id')


        # Changing field 'Order.delivery_address'
        db.alter_column('products_order', 'delivery_address_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['contacts.Address']))

    models = {
        'categories.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'default': "''"}),
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
            'addressed_as_custom': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'default': "''"}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'null': 'True', 'to': "orm['categories.Category']"}),
            'company': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'default': "''"}),
            'company_or_individual': ('django.db.models.fields.CharField', [], {'max_length': '10', 'default': "'individual'"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'department': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_artist': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'job_title': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'default': "''"}),
            'main_address': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'main_address'", 'null': 'True', 'to': "orm['contacts.Address']"}),
            'main_phonenumber': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'main_phonenumber'", 'null': 'True', 'to': "orm['contacts.PhoneNumber']"}),
            'migration_id': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name_first': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'default': "''"}),
            'name_last': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'default': "''"}),
            'name_middle': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'default': "''"}),
            'reference': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'default': "''"}),
            'suffix': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'default': "''"}),
            'title': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'default': "''"}),
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
        },
        'products.order': {
            'Meta': {'object_name': 'Order'},
            'comment': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'default': "''"}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts.Contact']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'delivery_address': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'default': 'None', 'related_name': "'deliveries'", 'null': 'True', 'to': "orm['contacts.Address']"}),
            'delivery_note': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_address': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'invoices'", 'null': 'True', 'to': "orm['contacts.Address']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'products.orderitem': {
            'Meta': {'object_name': 'OrderItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'item_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Order']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'qty': ('django.db.models.fields.IntegerField', [], {})
        },
        'products.product': {
            'Meta': {'object_name': 'Product'},
            'colour': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'has_colour': ('django.db.models.fields.BooleanField', [], {}),
            'has_size': ('django.db.models.fields.BooleanField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initials_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'item_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'size': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'max_digits': '5', 'decimal_places': '2'}),
            'stock_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['products']