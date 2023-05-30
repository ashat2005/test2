# Generated by Django 4.2.1 on 2023-05-25 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0003_setting_about_setting_email_setting_resource_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=255, verbose_name='Всего курсов')),
                ('students', models.CharField(max_length=255, verbose_name='Всего студентов')),
                ('positions', models.CharField(max_length=255, verbose_name='Глобальная позиция')),
            ],
            options={
                'verbose_name': 'Настройки достижения',
                'verbose_name_plural': 'Настройки достижения',
            },
        ),
    ]
