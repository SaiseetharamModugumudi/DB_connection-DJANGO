from django.contrib import admin
from app1.models import Students
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'enrollment_date', 'age')
    search_fields = ('first_name', 'age')
    ordering= ('enrollment_date',)

admin.site.register(Students,StudentAdmin)    