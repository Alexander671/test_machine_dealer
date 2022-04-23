from django.contrib import admin
from .models import Dealer
# Register your models here.

class DealerAdmin(admin.ModelAdmin):
    list_display = ('id','name','official', 'address')

admin.site.register(Dealer, DealerAdmin)