# Generated by Django 4.1.7 on 2023-02-15 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_contact_delete_category_delete_plan_delete_rewiews'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='image1',
            field=models.ImageField(default=1, upload_to='media/image1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='image2',
            field=models.ImageField(default=1, upload_to='media/image2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='image3',
            field=models.ImageField(default=1, upload_to='media/image3'),
            preserve_default=False,
        ),
    ]
