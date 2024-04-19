# Generated by Django 5.0.4 on 2024-04-19 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_filme_lancamento_alter_filme_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='tipo',
            field=models.CharField(choices=[('SERIE', 'Série'), ('FILME', 'Filme')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]
