# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Shortcut'
        db.create_table(u'laconicurls_shortcut', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'laconicurls', ['Shortcut'])

        # Adding unique constraint on 'Shortcut', fields ['content_type', 'object_id']
        db.create_unique(u'laconicurls_shortcut', ['content_type_id', 'object_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Shortcut', fields ['content_type', 'object_id']
        db.delete_unique(u'laconicurls_shortcut', ['content_type_id', 'object_id'])

        # Deleting model 'Shortcut'
        db.delete_table(u'laconicurls_shortcut')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'laconicurls.shortcut': {
            'Meta': {'unique_together': "(('content_type', 'object_id'),)", 'object_name': 'Shortcut'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['laconicurls']