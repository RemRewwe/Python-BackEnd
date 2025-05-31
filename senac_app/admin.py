from django.contrib import admin
from .models import Curso
from .models import UserProfile

admin.site.register(Curso)
admin.site.register(UserProfile)