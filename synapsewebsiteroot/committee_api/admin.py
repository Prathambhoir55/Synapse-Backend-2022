from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Faculty)
admin.site.register(Exmembers)
admin.site.register(CoreCommittee)
admin.site.register(Contact_info)
admin.site.register(multi_image)

class multi_image_Admin(admin.StackedInline):
    model = multi_image
 
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [multi_image_Admin]
    class Meta:
       model = Event
 


