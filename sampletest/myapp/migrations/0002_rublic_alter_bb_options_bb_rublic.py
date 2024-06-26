# Generated by Django 4.1 on 2024-04-20 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rublic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Рубрика',
                'verbose_name_plural': 'Рубирики',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='bb',
            options={'ordering': ['-published', 'title'], 'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AddField(
            model_name='bb',
            name='rublic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='myapp.rublic', verbose_name='Рубрика'),
        ),
    ]
