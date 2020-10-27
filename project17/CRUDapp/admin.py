from django.contrib import admin
from CRUDapp.models import Student
# Register your models here

class StudentAdmin(admin.ModelAdmin):
    '''
        Admin View for 
    '''
    list_display = ('student_name','student_mail','student_phoneno','student_address')

admin.site.register(Student, StudentAdmin)