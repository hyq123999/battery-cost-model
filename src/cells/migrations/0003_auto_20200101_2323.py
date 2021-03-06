# Generated by Django 2.2.5 on 2020-01-02 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cells', '0002_auto_20200101_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cellinput',
            name='alfoilthickness',
            field=models.DecimalField(db_column='alFoilThickness', decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='cellinput',
            name='anactivefrac',
            field=models.DecimalField(db_column='anActiveFrac', decimal_places=4, max_digits=20),
        ),
        migrations.AlterField(
            model_name='cellinput',
            name='anbinderfrac',
            field=models.DecimalField(db_column='anBinderFrac', decimal_places=4, max_digits=20),
        ),
        migrations.AlterField(
            model_name='cellinput',
            name='anconductorfrac',
            field=models.DecimalField(db_column='anConductorFrac', decimal_places=4, max_digits=20),
        ),
        migrations.AlterField(
            model_name='cellinput',
            name='angravcapacity',
            field=models.DecimalField(db_column='anGravCapacity', decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='cellinput',
            name='avgdischargevoltage',
            field=models.DecimalField(db_column='avgDischargeVoltage', decimal_places=3, max_digits=20),
        ),
        migrations.AlterField(
            model_name='cellinput',
            name='catactivefrac',
            field=models.DecimalField(db_column='catActiveFrac', decimal_places=4, max_digits=20),
        ),
        migrations.AlterField(
            model_name='cellinput',
            name='catbinderfrac',
            field=models.DecimalField(db_column='catBinderFrac', decimal_places=4, max_digits=20),
        ),
        migrations.AlterField(
            model_name='cellinput',
            name='catconductorfrac',
            field=models.DecimalField(db_column='catConductorFrac', decimal_places=4, max_digits=20),
        ),
        migrations.AlterField(
            model_name='cellinput',
            name='catgravcapacity',
            field=models.DecimalField(db_column='catGravCapacity', decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='cellinput',
            name='cattotalloading',
            field=models.DecimalField(db_column='catTotalLoading', decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='cellinput',
            name='cufoilthickness',
            field=models.DecimalField(db_column='cuFoilThickness', decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='cellinput',
            name='electrodelength',
            field=models.DecimalField(db_column='electrodeLength', decimal_places=3, max_digits=20),
        ),
        migrations.AlterField(
            model_name='cellinput',
            name='electrodewidth',
            field=models.DecimalField(db_column='electrodeWidth', decimal_places=3, max_digits=20),
        ),
        migrations.AlterField(
            model_name='cellinput',
            name='npratio',
            field=models.DecimalField(db_column='npRatio', decimal_places=3, max_digits=20),
        ),
    ]
