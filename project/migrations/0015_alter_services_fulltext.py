# Generated by Django 4.1.7 on 2023-02-17 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_services_fulltext_services_imagefull'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='fulltext',
            field=models.TextField(max_length=14000, null=True),
        ),
    ]
