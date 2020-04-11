from django.contrib import admin
from .models import Complain
# Register your models here.

@admin.register(Complain)
class ComplainAdmin(admin.ModelAdmin):
    class Meta:
        model = Complain