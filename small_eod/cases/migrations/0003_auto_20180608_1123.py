# Generated by Django 2.0.5 on 2018-06-08 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0002_auto_20180608_0331'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='tags',
            field=models.ManyToManyField(blank=True, to='cases.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='letter',
            name='channel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cases.Channel', verbose_name='Channel'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='institution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cases.Institution', verbose_name='Institution'),
        ),
    ]
