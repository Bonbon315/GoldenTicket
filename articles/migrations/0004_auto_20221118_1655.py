# Generated by Django 3.2.13 on 2022-11-18 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20221118_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playdetail',
            name='guidance',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='playdetail',
            name='locationname',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='playdetail',
            name='playcast',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='playdetail',
            name='playname',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='playdetail',
            name='ticketprice',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
