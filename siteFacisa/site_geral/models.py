from django.db import models

class User(models.Model):
    nome = models.CharField(max_length=264,unique=True)
    tag = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.name
        
class AccessRecord(models.Model):
    name = models.ForeignKey(User,on_delete=models.PROTECT)
    date = models.DateField()

    def __str__(self):
        return str(self.date)