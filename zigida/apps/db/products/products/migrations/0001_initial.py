# Generated by Django 3.2.4 on 2021-07-06 15:56

import django.contrib.postgres.fields
from django.db import migrations, models
import uuid
import zigida.apps.db.products.products.models
import zigida.core.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='DATE CREATED')),
                ('datetime_updated', models.DateTimeField(auto_now=True, verbose_name='DATE UPDATED')),
                ('last_updated_by', models.CharField(blank=True, max_length=50, null=True, verbose_name='LAST UPDATED BY')),
                ('bool_deleted', models.BooleanField(default=False, verbose_name='IS DELETED?')),
                ('uuid_code', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_key', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True, verbose_name='TOKEN')),
                ('code', models.CharField(default=zigida.core.utils.prod_randcode_gen, max_length=100, verbose_name='CODE')),
                ('title', models.CharField(blank=True, max_length=250, null=True, verbose_name='TITLE')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='SLUG')),
                ('image', models.ImageField(blank=True, null=True, upload_to=zigida.apps.db.products.products.models.products_img_path, verbose_name='PRODUCT IMAGE')),
                ('description', models.TextField(blank=True, null=True, verbose_name='DESCRIPTION')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=19, verbose_name='PRICE')),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=19, verbose_name='DISCOUNTED PRICE')),
                ('label', models.CharField(blank=True, max_length=250, null=True, verbose_name='TITLE')),
                ('category', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=999, verbose_name='CATEGORY'), default=zigida.apps.db.products.products.models.categories_array, null=True, size=None)),
                ('bool_active', models.BooleanField(default=True, verbose_name='IS ACTIVE')),
            ],
            options={
                'verbose_name_plural': 'products',
                'db_table': 'products',
            },
        ),
    ]
