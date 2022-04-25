from pyexpat import model
from django.contrib import admin
from jmespath import search

from .models import Training

# Register your models here.


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):

    list_display = ["name","trainer"]

    list_display_links = ["name","trainer"]

    search_fields = ["name"]
    
    list_filter = ["name"]
    class Meta:
        model = Training