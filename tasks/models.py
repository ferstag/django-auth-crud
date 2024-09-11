from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True) #el texfield es para un campo de texto más largo.
    created = models.DateTimeField(auto_now_add=True) #datetimefield con auto now en true para crear la fecha automatica%
    datecompleted = models.DateTimeField(null=True, blank=True) #se coloca el campo como vacio inicialmente.
    important = models.BooleanField(default=False) # las tareas por default no son importantes(hay que marcarlas en True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # cuando se elimina la primary key, se elimina el usuario en la tabla relacionada.
    def __str__(self):
        return self.title + '- by ' + self.user.username