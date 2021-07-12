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
            name='OpeningHour',
            fields=[
                ('street_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Street Name')),
                ('house_number', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Number')),
                ('post_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Postal Code')),
                ('area', models.CharField(blank=True, max_length=100, null=True, verbose_name='Area')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='City')),
                ('region', models.CharField(blank=True, max_length=100, null=True, verbose_name='Region')),
                ('country', django_countries.fields.CountryField(max_length=2, null=True, verbose_name='Country')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='DATE CREATED')),
                ('datetime_updated', models.DateTimeField(auto_now=True, verbose_name='DATE UPDATED')),
                ('last_updated_by', models.CharField(blank=True, max_length=50, null=True, verbose_name='LAST UPDATED BY')),
                ('bool_deleted', models.BooleanField(default=False, verbose_name='IS DELETED?')),
                ('uuid_code', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_key', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True, verbose_name='TOKEN')),
                ('code', models.CharField(default=zigida.core.utils.randcode_gen, max_length=100, verbose_name='CODE')),
                ('weekday', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Sunday'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')], null=True, verbose_name='WEEK DAY')),
                ('hour_from', models.TimeField(blank=True, null=True, verbose_name='HOUR FROM')),
                ('hour_to', models.TimeField(blank=True, null=True, verbose_name='HOUR FROM')),
            ],
            options={
                'verbose_name_plural': 'openinghours',
                'db_table': 'openinghours',
            },
        ),
    ]
