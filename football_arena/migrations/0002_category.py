# Generated by Django 4.2.3 on 2023-08-30 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football_arena', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_category', models.CharField(max_length=200)),
            ],
        ),
    ]