# Generated by Django 4.0.3 on 2022-04-11 06:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlemodel',
            name='posted_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 4, 11, 6, 19, 20, 849420, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articlemodel',
            name='posted_by',
            field=models.ForeignKey(default='MasterUser', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='投稿者'),
        ),
        migrations.AddField(
            model_name='articlemodel',
            name='posted_text',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
