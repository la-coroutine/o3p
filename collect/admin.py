from django.contrib import admin

from .models import Collect, Contribution, CollectItem

class ContributionAdmin(admin.TabularInline):
    model = Contribution

class CollectItemAdmin(admin.TabularInline):    
    model = CollectItem
    
class CollectAdmin(admin.ModelAdmin):
    model = Collect
    inlines = (
        CollectItemAdmin,
        )

    list_display = ('label', 'deadline', 'collected_amount', 'target_amount')


    

admin.site.register(Collect, CollectAdmin)
