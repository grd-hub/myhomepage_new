# Generated by Django 4.0.6 on 2022-07-22 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InformationEnglish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guestbook_text', models.TextField()),
                ('contact_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='InformationGerman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guestbook_text', models.TextField()),
                ('contact_text', models.TextField()),
            ],
        ),
    ]
