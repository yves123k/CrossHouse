# Generated by Django 4.0.6 on 2022-10-08 21:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CrossApp', '0006_remove_create_ad_comment_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='create_ad',
            name='comments_text',
        ),
        migrations.AddField(
            model_name='comments',
            name='comments_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment_user', to='CrossApp.create_ad'),
        ),
        migrations.AlterField(
            model_name='create_ad',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='create_ad', to=settings.AUTH_USER_MODEL),
        ),
    ]
