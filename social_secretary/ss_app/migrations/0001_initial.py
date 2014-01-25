# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contacts'
        db.create_table(u'ss_app_contacts', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('rank', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('facebook_id', self.gf('django.db.models.fields.BigIntegerField')()),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'ss_app', ['Contacts'])


    def backwards(self, orm):
        # Deleting model 'Contacts'
        db.delete_table(u'ss_app_contacts')


    models = {
        u'ss_app.contacts': {
            'Meta': {'object_name': 'Contacts'},
            'facebook_id': ('django.db.models.fields.BigIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'rank': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['ss_app']