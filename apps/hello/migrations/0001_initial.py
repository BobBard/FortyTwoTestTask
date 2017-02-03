# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'UserData'
        db.create_table(u'hello_userdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('bio', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('birth_date', self.gf('django.db.models.fields.DateField')()),
            ('jabber', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('other_contacts', self.gf('django.db.models.fields.TextField')(max_length=300)),
        ))
        db.send_create_signal(u'hello', ['UserData'])

    def backwards(self, orm):
        # Deleting model 'UserData'
        db.delete_table(u'hello_userdata')

    models = {
        u'hello.userdata': {
            'Meta': {'object_name': 'UserData'},
            'bio': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['hello']
