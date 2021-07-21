from django.contrib import admin

from .models import destination
from  .models import team

# Register your models here.
admin.site.register(destination)
admin.site.register(team)
