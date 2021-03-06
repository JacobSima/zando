# Generated by Django 3.2.4 on 2021-07-06 15:56

from django.db import migrations, models
import django_countries.fields
import uuid
import zigida.core.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='DATE CREATED')),
                ('datetime_updated', models.DateTimeField(auto_now=True, verbose_name='DATE UPDATED')),
                ('last_updated_by', models.CharField(blank=True, max_length=50, null=True, verbose_name='LAST UPDATED BY')),
                ('bool_deleted', models.BooleanField(default=False, verbose_name='IS DELETED?')),
                ('uuid_code', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_key', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True, verbose_name='TOKEN')),
                ('code', models.CharField(default=zigida.core.utils.randcode_gen, max_length=100, verbose_name='CODE')),
                ('street_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='STREET NAME')),
                ('apartment_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='HOME NUMBER')),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True, verbose_name='COUNTRY CODE')),
                ('zipcode', models.CharField(blank=True, max_length=100, null=True, verbose_name='POSTAL')),
                ('address_type', models.CharField(blank=True, choices=[('B', 'Billing'), ('S', 'Shipping')], max_length=1, null=True, verbose_name='ADDRESS TYPE')),
                ('payment_option', models.CharField(blank=True, max_length=100, null=True, verbose_name='PAYMENT OPTION')),
                ('default', models.BooleanField(blank=True, default=False, null=True, verbose_name='DEFAULT ADDRESS')),
            ],
            options={
                'verbose_name_plural': 'addresses',
                'db_table': 'addresses',
            },
        ),
    ]
