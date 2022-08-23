# Generated by Django 4.0.5 on 2022-06-08 11:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0003_alter_article_like_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='like_users',
            field=models.ManyToManyField(blank=True, null=True, related_name='like_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]