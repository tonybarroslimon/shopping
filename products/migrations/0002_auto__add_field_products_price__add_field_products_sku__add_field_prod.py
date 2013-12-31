# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Products.price'
        db.add_column('products_products', 'price',
                      self.gf('django.db.models.fields.IntegerField')(default=0.0),
                      keep_default=False)

        # Adding field 'Products.sku'
        db.add_column('products_products', 'sku',
                      self.gf('django.db.models.fields.CharField')(default='abc', max_length=160),
                      keep_default=False)

        # Adding field 'Products.inventory'
        db.add_column('products_products', 'inventory',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Products.price'
        db.delete_column('products_products', 'price')

        # Deleting field 'Products.sku'
        db.delete_column('products_products', 'sku')

        # Deleting field 'Products.inventory'
        db.delete_column('products_products', 'inventory')


    models = {
        'products.products': {
            'Meta': {'object_name': 'Products'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'inventory': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '0.0'}),
            'sku': ('django.db.models.fields.CharField', [], {'default': "'abc'", 'max_length': '160'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['products']