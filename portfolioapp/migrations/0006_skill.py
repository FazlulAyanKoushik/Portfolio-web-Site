# Generated by Django 3.0.8 on 2020-08-16 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0005_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
    ]
