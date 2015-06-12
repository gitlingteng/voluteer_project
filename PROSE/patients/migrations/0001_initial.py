# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Patient'
        db.create_table('patients_patient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_last', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name_first', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=101, null=True, blank=True)),
            ('dob', self.gf('django.db.models.fields.DateField')()),
            ('dod', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('mrn', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('transplant', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dot', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patients.Diagnosis'], null=True, blank=True)),
            ('language', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('clinic_day', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='creator', to=orm['auth.User'])),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='modifier', null=True, to=orm['auth.User'])),
        ))
        db.send_create_signal('patients', ['Patient'])

        # Adding M2M table for field attendings on 'Patient'
        db.create_table('patients_patient_attendings', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('patient', models.ForeignKey(orm['patients.patient'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('patients_patient_attendings', ['patient_id', 'user_id'])

        # Adding M2M table for field fellows on 'Patient'
        db.create_table('patients_patient_fellows', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('patient', models.ForeignKey(orm['patients.patient'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('patients_patient_fellows', ['patient_id', 'user_id'])

        # Adding M2M table for field nps on 'Patient'
        db.create_table('patients_patient_nps', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('patient', models.ForeignKey(orm['patients.patient'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('patients_patient_nps', ['patient_id', 'user_id'])

        # Adding M2M table for field ppus on 'Patient'
        db.create_table('patients_patient_ppus', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('patient', models.ForeignKey(orm['patients.patient'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('patients_patient_ppus', ['patient_id', 'user_id'])

        # Adding model 'Diagnosis'
        db.create_table('patients_diagnosis', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('accepted_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('patients', ['Diagnosis'])


    def backwards(self, orm):
        # Deleting model 'Patient'
        db.delete_table('patients_patient')

        # Removing M2M table for field attendings on 'Patient'
        db.delete_table('patients_patient_attendings')

        # Removing M2M table for field fellows on 'Patient'
        db.delete_table('patients_patient_fellows')

        # Removing M2M table for field nps on 'Patient'
        db.delete_table('patients_patient_nps')

        # Removing M2M table for field ppus on 'Patient'
        db.delete_table('patients_patient_ppus')

        # Deleting model 'Diagnosis'
        db.delete_table('patients_diagnosis')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'patients.diagnosis': {
            'Meta': {'ordering': "['name']", 'object_name': 'Diagnosis'},
            'accepted_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
        },
        'patients.patient': {
            'Meta': {'object_name': 'Patient'},
            'attendings': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'attendings'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'clinic_day': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'creator'", 'to': "orm['auth.User']"}),
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.Diagnosis']", 'null': 'True', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {}),
            'dod': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'dot': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fellows': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'fellows'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'modifier'", 'null': 'True', 'to': "orm['auth.User']"}),
            'mrn': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '101', 'null': 'True', 'blank': 'True'}),
            'name_first': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_last': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nps': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'nps'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'ppus': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'ppus'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'transplant': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['patients']