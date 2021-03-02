from django.contrib import admin
from assignments.models import Assignment


class AssignmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Assignment, AssignmentAdmin)
