from django.contrib import admin
from pages.models import *

admin.site.register(Diagnostic)
admin.site.register(User)
admin.site.register(Programme)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(AssignedCourses)
admin.site.register(ProgrammeCourses)