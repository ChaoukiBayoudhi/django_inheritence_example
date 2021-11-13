from django.contrib import admin

from .models import Terminal,Bechelor

# Register your models here.
#admin.site.register(Bechelor)
#admin.site.register(Terminal)
#or
admin.site.register([Terminal,Bechelor])