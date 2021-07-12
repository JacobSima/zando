# Generated by Django 3.2.4 on 2021-07-06 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payments', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('locations', '0001_initial'),
        ('receipts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='receipts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='receipt',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='receipts', to='locations.location'),
        ),
        migrations.AddField(
            model_name='receipt',
            name='payment',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='receipts', to='payments.payment'),
        ),
    ]