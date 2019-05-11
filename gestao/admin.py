from django.contrib import admin
from . models import Animal, Creator, Farm

admin.site.register(Animal)
admin.site.register(Creator)
admin.site.register(Farm)