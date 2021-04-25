# Generated by Django 3.1.7 on 2021-04-24 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaseMailingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email подписчика')),
            ],
            options={
                'db_table': 'case_mailing_list',
            },
        ),
        migrations.CreateModel(
            name='CommonMailingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email подписчика')),
            ],
            options={
                'db_table': 'common_mailing_list',
            },
        ),
    ]