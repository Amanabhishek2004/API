# Generated by Django 4.1.7 on 2023-08-31 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='link',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
