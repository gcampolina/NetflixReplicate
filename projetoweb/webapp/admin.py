from django.contrib import admin
from .models import CustomUser
from .models import Filme

admin.site.register(Filme)
admin.site.register(CustomUser)