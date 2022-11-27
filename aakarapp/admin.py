# from django.contrib import admin

# from .models import TaskZero
# from .models import TaskOne
# # Register your models here.

# admin.site.register(TaskZero)
# admin.site.register(TaskOne)
from django.contrib import admin

from . models import TaskZero
# from . models import TaskOne
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(TaskZero)
# @admin.register(TaskOne)
class userdetail(ImportExportModelAdmin):
    pass