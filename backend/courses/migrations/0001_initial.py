# Generated by Django 4.2.20 on 2025-05-05 07:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, verbose_name='Название')),
                ('category_description', models.TextField(max_length=250, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=255, unique=True, verbose_name='Название курса')),
                ('course_duration', models.PositiveIntegerField(default=1, verbose_name='Длительность курса (мес.)')),
                ('course_date_of_start', models.DateField(verbose_name='Дата начала курса')),
                ('course_price', models.FloatField(default=1, verbose_name='Цена курса (в руб.)')),
                ('course_description', models.TextField(max_length=750, verbose_name='Описание курса')),
                ('course_for_who', models.CharField(choices=[('Для начинающих', 'Для начинающих'), ('Для продолжающих', 'Для продолжающих'), ('Для продвинутых', 'Для продвинутых'), ('Для всех', 'Для всех')], max_length=150, verbose_name='Для кого')),
                ('course_picture', models.ImageField(blank=True, null=True, upload_to='course_picture/', verbose_name='Картинка курса')),
                ('is_arhived', models.BooleanField(default=False, verbose_name='Архивирован ли курс')),
                ('course_categories', models.ManyToManyField(to='courses.categories', verbose_name='Категории')),
                ('course_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Преподаватель курса')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_name', models.CharField(max_length=255, verbose_name='Название материала')),
                ('material_description', models.TextField(max_length=500, verbose_name='Описание материала')),
                ('file', models.FileField(blank=True, null=True, upload_to='dop_materials/', verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'Дополнительный материал',
                'verbose_name_plural': 'Дополнительные материалы',
            },
        ),
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_name', models.CharField(max_length=255, verbose_name='Название урока')),
                ('lesson_number', models.PositiveIntegerField(default=0, verbose_name='Номер урока в курсе')),
                ('lesson_description', models.TextField(max_length=300, verbose_name='Описание урока')),
                ('video_file', models.FileField(blank=True, null=True, upload_to='video_materials/', verbose_name='Видеоматериал к уроку')),
                ('text_file', models.FileField(blank=True, null=True, upload_to='text_materials/', verbose_name='Текстовый файл к уроку')),
                ('lesson_course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='courses.courses', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
                'ordering': ['lesson_number'],
            },
        ),
    ]
