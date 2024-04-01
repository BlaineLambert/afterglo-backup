# Generated by Django 4.2.6 on 2024-04-01 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.IntegerField()),
                ('desc', models.TextField()),
                ('photo', models.ImageField(blank=True, default='app/uploads/default.png', null=True, upload_to='app/uploads/')),
            ],
        ),
    ]
