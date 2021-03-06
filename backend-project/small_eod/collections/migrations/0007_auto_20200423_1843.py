# Generated by Django 3.0.5 on 2020-04-23 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections', '0006_auto_20200423_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='comments',
            field=models.CharField(blank=True, help_text='Comments for collection.', max_length=256, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='queries',
            field=models.CharField(help_text='Queries for collection.', max_length=256, verbose_name='Queries'),
        ),
    ]
