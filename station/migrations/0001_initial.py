# Generated by Django 5.1.6 on 2025-02-15 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=244, null=True)),
                ('num_seats', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'buses',
            },
        ),
    ]
