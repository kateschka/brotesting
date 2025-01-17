# Generated by Django 5.1.4 on 2025-01-17 14:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=200, verbose_name='Текст ответа'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='is_correct',
            field=models.BooleanField(default=False, verbose_name='Правильный ответ'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.question', verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(related_name='enrolled_courses', to=settings.AUTH_USER_MODEL, verbose_name='Студенты'),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='question',
            name='points',
            field=models.IntegerField(default=1, verbose_name='Баллы'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(verbose_name='Текст вопроса'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('MCQ', 'Multiple Choice'), ('TF', 'True/False'), ('SA', 'Short Answer')], max_length=3, verbose_name='Тип вопроса'),
        ),
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.quiz', verbose_name='Тест'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.course', verbose_name='Дисциплина'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='passing_score',
            field=models.IntegerField(verbose_name='Проходной балл'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='time_limit',
            field=models.IntegerField(verbose_name='Ограничение по времени'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='quizattempt',
            name='completed_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата завершения'),
        ),
        migrations.AlterField(
            model_name='quizattempt',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.quiz', verbose_name='Тест'),
        ),
        migrations.AlterField(
            model_name='quizattempt',
            name='score',
            field=models.FloatField(blank=True, null=True, verbose_name='Баллы'),
        ),
        migrations.AlterField(
            model_name='quizattempt',
            name='started_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата начала'),
        ),
        migrations.AlterField(
            model_name='quizattempt',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Студент'),
        ),
        migrations.AlterField(
            model_name='quizsettings',
            name='allow_review',
            field=models.BooleanField(default=True, verbose_name='Разрешить пересмотр'),
        ),
        migrations.AlterField(
            model_name='quizsettings',
            name='max_attempts',
            field=models.IntegerField(default=1, verbose_name='Максимальное количество попыток'),
        ),
        migrations.AlterField(
            model_name='quizsettings',
            name='quiz',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.quiz', verbose_name='Тест'),
        ),
        migrations.AlterField(
            model_name='quizsettings',
            name='show_results_immediately',
            field=models.BooleanField(default=True, verbose_name='Показывать результаты сразу'),
        ),
        migrations.AlterField(
            model_name='quizsettings',
            name='shuffle_questions',
            field=models.BooleanField(default=False, verbose_name='Перемешать вопросы'),
        ),
        migrations.AlterField(
            model_name='studentanswer',
            name='attempt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.quizattempt', verbose_name='Попытка'),
        ),
        migrations.AlterField(
            model_name='studentanswer',
            name='is_correct',
            field=models.BooleanField(null=True, verbose_name='Правильный ответ'),
        ),
        migrations.AlterField(
            model_name='studentanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.question', verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='studentanswer',
            name='selected_choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.choice', verbose_name='Выбранный ответ'),
        ),
        migrations.AlterField(
            model_name='studentanswer',
            name='text_answer',
            field=models.TextField(blank=True, null=True, verbose_name='Текстовый ответ'),
        ),
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('graduation_year', models.IntegerField(verbose_name='Год выпуска')),
                ('courses', models.ManyToManyField(related_name='groups', to='core.course', verbose_name='Дисциплины')),
                ('students', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Студенты')),
            ],
        ),
    ]
