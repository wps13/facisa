from django.db import models

"""
Classe para dados referentes ao usuário ,como nome(name) e tag
"""
class User(models.Model):
    name = models.CharField(max_length=264,unique=True)
    tag = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.name


"""
Classe com dados referentes ao histórico de acessos, contendo nome do usuário(name) e a data de acesso(date)
"""
class AccessRecord(models.Model):
    name = models.ForeignKey(User,on_delete=models.PROTECT)
    date = models.DateField()

    def __str__(self):
        return str(self.date)