# Generated by Django 2.1.2 on 2018-10-27 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='article',
            unique_together=set(),
        ),
    ]
