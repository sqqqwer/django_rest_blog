# Generated by Django 3.2.16 on 2024-10-27 05:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20241027_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='follow',
            name='follow_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 10, 27, 5, 46, 31, 208124, tzinfo=utc), verbose_name='Дата подписки'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='unique_follow'),
        ),
    ]
