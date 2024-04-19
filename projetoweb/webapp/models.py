from django.db import models
from django.contrib.auth.models import AbstractUser, User



class Filme(models.Model):
    
    categorias = (
        ('ACAO', 'Ação'),
        ('AVENTURA', 'Aventura'),
        ('COMEDIA', 'Comédia'),
        ('DRAMA', 'Drama'),
        ('TERROR', 'Terror'),
        ('ROMANCE', 'Romance'),
        ('SCI_FI', 'Ficção Científica')
    )
    lancamento = (
        ('SIM', 'Sim'),
        ('NAO', 'Não')
    )
    tipo = (
        ('SERIE', 'Série'),
        ('FILME', 'Filme')
    )

    original_netflix = (
        ('SIM', 'Sim'),
        ('NAO', 'Não')
    )

    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    categoria = models.CharField(max_length=100, choices=categorias)
    lancamento = models.CharField(max_length=100, choices=lancamento)
    tipo = models.CharField(max_length=100, choices=tipo)
    original_netflix = models.CharField(max_length=100, choices=original_netflix)
    imagem = models.ImageField(upload_to='filmes/')

    def __str__(self):
        return self.nome




class CustomUser(AbstractUser):
     foto = models.ImageField(
        upload_to='fotos_perfil/',
        blank=True,
        null=True,
        default='fotos_perfil/netflix-avatar.png'
    )

     def __str__(self):
        return self.username