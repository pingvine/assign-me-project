from django.contrib import admin
from handins.models import Handin, Assignment


class HandinAdmin(admin.ModelAdmin):
    pass


class AssignmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Handin, HandinAdmin)
admin.site.register(Assignment, AssignmentAdmin)
