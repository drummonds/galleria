# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Category.name'
        db.alter_column('categories_category', 'name', self.gf('django.db.models.fields.CharField')(max_length=40))

    def backwards(self, orm):

        # Changing field 'Category.name'
        db.alter_column('categories_category', 'name', self.gf('django.db.models.fields.CharField')(max_length=100))

    models = {
        'categories.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['categories']