# Generated by Django 4.0.4 on 2022-05-17 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_text', models.CharField(max_length=200)),
                ('article_text', models.CharField(max_length=1000)),
                ('pub_date', models.DateTimeField(verbose_name='date_published')),
            ],
        ),
    ]
