# Generated by Django 4.1 on 2024-04-20 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('content', models.TextField(verbose_name='Описание')),
                ('price', models.FloatField(verbose_name='Стоимость')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявление',
                'ordering': ['-published', 'title'],
            },
        ),
    ]
