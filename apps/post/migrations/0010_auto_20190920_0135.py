# Generated by Django 2.2.5 on 2019-09-19 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_auto_20190918_0042'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_date', 'id']},
        ),
    ]