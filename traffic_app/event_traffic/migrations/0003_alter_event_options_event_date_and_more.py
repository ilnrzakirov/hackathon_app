# Generated by Django 4.1.4 on 2022-12-18 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_traffic', '0002_student_alter_event_options_register_feedback'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Мероприятия', 'verbose_name_plural': 'Мероприятия'},
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата и время'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Текст отзыва'),
        ),
        migrations.AlterField(
            model_name='register',
            name='link',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Уникальная ссылка для отслеживания'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email'),
        ),
    ]
