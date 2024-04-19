# Generated by Django 5.0.4 on 2024-04-18 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_filme'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='lancamento',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='filme',
            name='categoria',
            field=models.CharField(choices=[('ACAO', 'Ação'), ('AVENTURA', 'Aventura'), ('COMEDIA', 'Comédia'), ('DRAMA', 'Drama'), ('TERROR', 'Terror'), ('ROMANCE', 'Romance'), ('SCI_FI', 'Ficção Científica')], max_length=100),
        ),
    ]
