# Generated by Django 3.2.19 on 2023-06-15 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Sport', 'Sport'), ('School', 'School'), ('Books', 'Books'), ('Person', 'Person'), ('Place', 'Place'), ('Event', 'Event'), ('Art', 'Art'), ('Media', 'Media'), ('Others', 'Others')], max_length=50),
        ),
    ]
