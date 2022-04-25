from django.contrib import admin

# Register your models here.

from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = ["name","attendance"]

    list_display_links = ["name","attendance"]

    search_fields = ["name"]
    
    list_filter = ["name"]
    class Meta:
        model = Customer