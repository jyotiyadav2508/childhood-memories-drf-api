# Generated by Django 3.2.19 on 2023-06-15 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
        ('comment_likes', '0003_auto_20230528_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentlikes',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_likes', to='comments.comment'),
        ),
    ]
