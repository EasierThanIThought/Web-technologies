# Generated by Django 3.2.9 on 2021-12-12 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Никнейм')),
                ('feedback', models.TextField(verbose_name='Отзыв')),
            ],
        ),
    ]
