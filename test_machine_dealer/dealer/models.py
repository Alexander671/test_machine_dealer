from django.db import models

# Create your models here.
class Dealer(models.Model): # Таблица дилеров которая наследует models.Model
    name = models.CharField(max_length=100) # название дилера
    official = models.BooleanField() # официальный ли диллер
    address = models.TextField() # адрес дилера
    class Meta:
        verbose_name = ("Dealer") # человекочитаемое имя объекта
        verbose_name_plural = ("Dealers")  #человекочитаемое множественное имя для Дилера
    def __str__(self):
        return self.name  # __str__ применяется для отображения объекта в интерфейсе