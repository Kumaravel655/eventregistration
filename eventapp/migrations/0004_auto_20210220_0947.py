# Generated by Django 3.1.1 on 2021-02-20 09:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0003_auto_20210220_0740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participatent',
            old_name='name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='participatent',
            name='mobile',
        ),
        migrations.AddField(
            model_name='participatent',
            name='phone',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='participatent',
            name='email',
            field=models.CharField(max_length=10),
        ),
    ]
