from django.contrib import admin
from .models import Project

#specify what folders we want to show up in the admin


admin.site.register(Project)