# Generated by Django 2.1.5 on 2019-02-06 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='age',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='website',
            name='seo_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='website',
            name='similar_websites',
            field=models.TextField(blank=True, null=True),
        ),
    ]
