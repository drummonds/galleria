# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Product.colour'
        db.alter_column('products_product', 'colour', self.gf('django.db.models.fields.CharField')(max_length=2))

    def backwards(self, orm):

        # Changing field 'Product.colour'
        db.alter_column('products_product', 'colour', self.gf('django.db.models.fields.CharField')(max_length=1))

    models = {
        'products.product': {
            'Meta': {'object_name': 'Product'},
            'colour': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'has_colour': ('django.db.models.fields.BooleanField', [], {}),
            'has_size': ('django.db.models.fields.BooleanField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initials_price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '6'}),
            'item_price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '6'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'size': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'blank': 'True', 'max_digits': '5'}),
            'stock_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['products']