# Generated by Django 2.0.2 on 2018-05-28 17:41

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('site_geral', '0003_auto_20180528_1420'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HistoricoAcessos',
            new_name='AccessRecord',
        ),
        migrations.RenameModel(
            old_name='Usuario',
            new_name='User',
        ),
        migrations.RenameField(
            model_name='accessrecord',
            old_name='dataAcesso',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='accessrecord',
            old_name='nome',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='nome',
            new_name='name',
        ),
    ]
