# Generated by Django 4.1.6 on 2023-02-15 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_alter_rewiews_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='movie/image_user')),
                ('prof', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('deviz', models.TextField(max_length=350)),
            ],
            options={
                'verbose_name_plural': 'Работники',
            },
        ),
    ]
