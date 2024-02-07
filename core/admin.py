from django.contrib import admin
from .models import *
# Register your models here.
class studentAdmin(admin.ModelAdmin):

    list_display = ('dars_nomi', 'uqituvchi', 'kirish_vaqti', 'chiqish_vaqti', 'student_name')
    list_filter = ('kirish_vaqti', 'chiqish_vaqti')
admin.site.register(student, studentAdmin)
admin.site.register(Uqituvchi)
admin.site.register(name)