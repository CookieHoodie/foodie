from django.contrib import admin
from .models import *

# Register your models here.
class OwnerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Owner, OwnerAdmin)

class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmin)