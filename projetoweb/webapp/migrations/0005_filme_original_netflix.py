# Generated by Django 5.0.4 on 2024-04-19 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_filme_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='original_netflix',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]
