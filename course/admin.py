from ast import ClassDef
from pyexpat import model
from django.contrib import admin
from .models import Courses, lessons
# Register your models here.
class LessonsInline(admin.StackedInline):
    model = lessons
    extra = 1

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display =("name", "description", "draft")
    inlines = [LessonsInline]
    save_on_top = True
    # save_as = True
    list_editable = ("draft",)
    
    fieldsets = (
        (None,{
            "fields": ("name", "description")
        }),
        (None,{
            "fields": (("term", "modul", "time"),)
        }),
        (None,{
            "fields": (("image","price"),)
        }),
        ("Options",{
            "fields": ("draft",)
        }),
    )

@admin.register(lessons)
class LessonsAdmin(admin.ModelAdmin):
    list_display =["course_name","title", "description"]
    list_filter = ("course_name", "title")
    search_fields = ("title",)


# admin.site.register(lessons) 