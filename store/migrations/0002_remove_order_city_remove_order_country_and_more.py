# Generated by Django 4.1.7 on 2023-04-14 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='city',
        ),
        migrations.RemoveField(
            model_name='order',
            name='country',
        ),
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
        migrations.RemoveField(
            model_name='order',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='order',
            name='state',
        ),
    ]