# Generated by Django 2.0.2 on 2018-02-11 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0004_auto_20180211_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='published_year',
            field=models.CharField(default=2016, max_length=4),
            preserve_default=False,
        ),
    ]