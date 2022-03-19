from django.contrib import admin
from .models import Headphone

class HeadphoneAdmin(admin.ModelAdmin):
  list = ('title', 'description')

admin.site.register(Headphone, HeadphoneAdmin)