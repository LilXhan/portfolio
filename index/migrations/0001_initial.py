# Generated by Django 4.1.5 on 2023-01-28 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=200)),
                ('is_routable', models.BooleanField()),
            ],
            options={
                'db_table': 'users_data',
            },
        ),
    ]
