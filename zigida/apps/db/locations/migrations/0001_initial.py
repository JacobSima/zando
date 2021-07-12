# Generated by Django 3.2.4 on 2021-07-06 15:56

from django.db import migrations, models
import uuid
import zigida.core.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='DATE CREATED')),
                ('datetime_updated', models.DateTimeField(auto_now=True, verbose_name='DATE UPDATED')),
                ('last_updated_by', models.CharField(blank=True, max_length=50, null=True, verbose_name='LAST UPDATED BY')),
                ('bool_deleted', models.BooleanField(default=False, verbose_name='IS DELETED?')),
                ('uuid_code', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=zigida.core.utils.randcode_gen, max_length=100, verbose_name='CODE')),
                ('ipaddress', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP ADDRESS')),
                ('macaddress', models.CharField(blank=True, max_length=100, null=True, verbose_name='MAC ADDRESS')),
                ('street', models.CharField(blank=True, max_length=100, null=True, verbose_name='STREET')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='CITY')),
                ('zip_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='POST CODE')),
                ('region', models.CharField(blank=True, max_length=100, null=True, verbose_name='REGION')),
                ('country_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='COUNTRY CODE.')),
                ('country_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='COUNTRY NAME')),
                ('lat', models.CharField(blank=True, max_length=100, null=True, verbose_name='LATITUDE')),
                ('lng', models.CharField(blank=True, max_length=100, null=True, verbose_name='LONGITUDE')),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='PHONE')),
                ('area_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='AREA CODE')),
                ('mcc', models.CharField(blank=True, max_length=100, null=True, verbose_name='MCC')),
                ('mnc', models.CharField(blank=True, max_length=100, null=True, verbose_name='MNC')),
                ('mobile_brand', models.CharField(blank=True, max_length=100, null=True, verbose_name='MOBILE BRAND')),
                ('device_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='DEVICE TYPE')),
                ('device_model', models.CharField(blank=True, max_length=100, null=True, verbose_name='DEVICE MODEL')),
                ('op_system', models.CharField(blank=True, max_length=100, null=True, verbose_name='OPERAT. SYS')),
                ('isp', models.CharField(blank=True, max_length=100, null=True, verbose_name='ISP')),
                ('domain', models.CharField(blank=True, max_length=100, null=True, verbose_name='DOMAIN')),
                ('timezone', models.CharField(blank=True, max_length=100, null=True, verbose_name='TIMEZONE')),
                ('netspeed', models.CharField(blank=True, max_length=100, null=True, verbose_name='NET SPEED')),
                ('idd_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='IDD CODE')),
                ('usage_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='USAGE TYPE')),
                ('weather_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='WEATHER CODE')),
                ('weather_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='WEATHER NAME')),
                ('bool_active', models.BooleanField(default=True, verbose_name='IS ACTIVE')),
            ],
            options={
                'verbose_name_plural': 'locations',
                'db_table': 'locations',
            },
        ),
    ]