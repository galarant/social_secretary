# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'Contacts', fields ['facebook_id']
        db.create_index(u'ss_app_contacts', ['facebook_id'])


    def backwards(self, orm):
        # Removing index on 'Contacts', fields ['facebook_id']
        db.delete_index(u'ss_app_contacts', ['facebook_id'])


    models = {
        u'ss_app.contacts': {
            'Meta': {'object_name': 'Contacts'},
            'facebook_id': ('django.db.models.fields.BigIntegerField', [], {'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'rank': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['ss_app']