# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Product'
        db.create_table('products_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('has_colour', self.gf('django.db.models.fields.BooleanField')()),
            ('colour', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('has_size', self.gf('django.db.models.fields.BooleanField')()),
            ('size', self.gf('django.db.models.fields.DecimalField')(blank=True, max_digits=5, decimal_places=2)),
            ('stock_quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('item_price', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('initials_price', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
        ))
        db.send_create_signal('products', ['Product'])


    def backwards(self, orm):
        # Deleting model 'Product'
        db.delete_table('products_product')


    models = {
        'products.product': {
            'Meta': {'object_name': 'Product'},
            'colour': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
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