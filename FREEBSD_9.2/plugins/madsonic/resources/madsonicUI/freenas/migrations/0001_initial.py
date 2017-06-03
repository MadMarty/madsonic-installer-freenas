# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Madsonic'
        db.create_table('freenas_madsonic', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('madsonic_max_memory', self.gf('django.db.models.fields.IntegerField')(default=150)),
            ('madsonic_ssl', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('madsonic_port', self.gf('django.db.models.fields.IntegerField')(default=4040)),
            ('madsonic_context_path', self.gf('django.db.models.fields.CharField')(default='/', max_length=120)),
        ))
        db.send_create_signal('freenas', ['Madsonic'])


    def backwards(self, orm):
        
        # Deleting model 'Madsonic'
        db.delete_table('freenas_madsonic')


    models = {
        'freenas.madsonic': {
            'Meta': {'object_name': 'Madsonic'},
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'madsonic_max_memory': ('django.db.models.fields.IntegerField', [], {'default': '150'}),
            'madsonic_ssl': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'madsonic_port': ('django.db.models.fields.IntegerField', [], {'default': '4040'}),
            'madsonic_context_path': ('django.db.models.fields.CharField', [], {'default': "'/'", 'max_length': '120'}),
        }
    }

    complete_apps = ['freenas']
