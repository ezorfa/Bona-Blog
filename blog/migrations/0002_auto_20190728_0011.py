# Generated by Django 2.2 on 2019-07-28 00:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_published',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]