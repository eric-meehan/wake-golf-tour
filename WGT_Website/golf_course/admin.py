from django.contrib import admin
from . models import GolfCourse, Hole

class HoleInline (admin.TabularInline):
    model = Hole
    max_num = 18
    can_delete = False
    exclude = ['hole_id']
    
class GolfCourseAdmin (admin.ModelAdmin):
    inlines = [HoleInline]
    fieldsets = [(None, {'fields': ['course_name', 'course_total_par']})]
    exclude = ['course_id']
    actions_on_top = False

# Register your models here.
admin.site.register(GolfCourse, GolfCourseAdmin)
