# Generated by Django 3.2.13 on 2022-11-18 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20221118_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationdetail',
            name='address',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='locationdetail',
            name='lat',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='locationdetail',
            name='lgt',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='locationdetail',
            name='locationid',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='locationdetail',
            name='locationname',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='locationdetail',
            name='phone',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='locationdetail',
            name='relateurl',
            field=models.CharField(max_length=500),
        ),
    ]