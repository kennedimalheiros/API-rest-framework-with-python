from django.db import models

class Agenda(models.Model):
    nome = models.CharField('Nome', max_length=40)
    telefone = models.CharField('Telefone', max_length=20)
    endereco = models.CharField('Endereço', max_length=50)
    email = models.EmailField('Email', max_length=50)

    def __str__(self):
        return self.nome + ' - Telefone: ' + self.telefone

