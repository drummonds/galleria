# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PhoneNumber'
        db.create_table(u'contacts_phonenumber', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Contact'])),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'contacts', ['PhoneNumber'])

        # Adding model 'Address'
        db.create_table(u'contacts_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Contact'])),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('county', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'contacts', ['Address'])

        # Adding model 'Note'
        db.create_table(u'contacts_note', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Contact'])),
            ('note', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'contacts', ['Note'])

        # Adding model 'Contact'
        db.create_table(u'contacts_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.ContactType'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('name_first', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name_middle', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('name_last', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('suffix', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('addressed_as', self.gf('django.db.models.fields.CharField')(default='custom', max_length=10)),
            ('addressed_as_custom', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('reference', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('company_or_individual', self.gf('django.db.models.fields.CharField')(default='individual', max_length=10)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('job_title', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('departament', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('main_phonenumber', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, null=True, related_name='main_phonenumber', to=orm['contacts.PhoneNumber'])),
            ('main_address', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, null=True, related_name='main_address', to=orm['contacts.Address'])),
        ))
        db.send_create_signal(u'contacts', ['Contact'])

        # Adding M2M table for field categories on 'Contact'
        m2m_table_name = db.shorten_name(u'contacts_contact_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contact', models.ForeignKey(orm[u'contacts.contact'], null=False)),
            ('category', models.ForeignKey(orm[u'categories.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['contact_id', 'category_id'])


    def backwards(self, orm):
        # Deleting model 'PhoneNumber'
        db.delete_table(u'contacts_phonenumber')

        # Deleting model 'Address'
        db.delete_table(u'contacts_address')

        # Deleting model 'Note'
        db.delete_table(u'contacts_note')

        # Deleting model 'Contact'
        db.delete_table(u'contacts_contact')

        # Removing M2M table for field categories on 'Contact'
        db.delete_table(db.shorten_name(u'contacts_contact_categories'))


    models = {
        u'categories.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'contacts.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Contact']"}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'contacts.contact': {
            'Meta': {'object_name': 'Contact'},
            'addressed_as': ('django.db.models.fields.CharField', [], {'default': "'custom'", 'max_length': '10'}),
            'addressed_as_custom': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['categories.Category']", 'symmetrical': 'False'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'company_or_individual': ('django.db.models.fields.CharField', [], {'default': "'individual'", 'max_length': '10'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'departament': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'main_address': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'main_address'", 'to': u"orm['contacts.Address']"}),
            'main_phonenumber': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'main_phonenumber'", 'to': u"orm['contacts.PhoneNumber']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name_first': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_last': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_middle': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.ContactType']"})
        },
        u'contacts.contacttype': {
            'Meta': {'object_name': 'ContactType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'contacts.note': {
            'Meta': {'object_name': 'Note'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Contact']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'note': ('django.db.models.fields.TextField', [], {})
        },
        u'contacts.phonenumber': {
            'Meta': {'object_name': 'PhoneNumber'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['contacts']