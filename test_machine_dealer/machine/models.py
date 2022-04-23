from django.db import models
from dealer.models import Dealer
# Create your models here.
class Machine(models.Model): # Таблица машин которая наследует models.Model
    machine_model = models.TextField() # модель машины
    date_of_create = models.DateField(auto_now_add=False) # дата выпуска машины
    dealer = models.ForeignKey(Dealer,on_delete=models.CASCADE, blank = True, null = True)
    price = models.IntegerField()
    class Meta:
        verbose_name = ("Machine") # человекочитаемое имя объекта
        verbose_name_plural = ("Machins")  #человекочитаемое множественное имя для Машины
    def __str__(self):
        return self.machine_model  # __str__ применяется для отображения объекта в интерфейсе