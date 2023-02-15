# Generated by Django 4.1.6 on 2023-02-15 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_category_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rewiews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('text', models.TextField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]