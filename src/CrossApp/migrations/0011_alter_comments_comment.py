# Generated by Django 4.0.6 on 2022-10-08 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrossApp', '0010_alter_comments_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.TextField(max_length=500),
        ),
    ]