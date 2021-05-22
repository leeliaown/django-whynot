from django.contrib import admin
from .models import Engineer, Task

# admin.site.register(Task)
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("user", "cr_date", "cr_description", "pm")
    list_filter = ('cr_date', 'pm',)

    # search_fields = ("pm__startswith", )

@admin.display(ordering='name')
@admin.register(Engineer)
class EngineerAdmin(admin.ModelAdmin):
    
    list_display = ("name", "eng_id")
    # list_filter = ("name", )
    search_fields = ("name__startswith", )
    # class Meta:
    #     ordering = ("name")
    
    # def save_model(self, request, obj, form, change):
    #     if not change:
    #         obj.pm = request.user
    #     obj.save()