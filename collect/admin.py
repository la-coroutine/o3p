from django.contrib import admin

from .models import Collect, CollectItem, Contribution

class ContributionAdmin(admin.TabularInline):
    model = Contribution

class CollectItemAdmin(admin.TabularInline):
    model = CollectItem

class CollectAdmin(admin.ModelAdmin):
    model = Collect
    inlines = (
        CollectItemAdmin,
        ContributionAdmin,
        )

    list_display = ('label', 'deadline', 'collected_amount', 'target_amount')

admin.site.register(Collect, CollectAdmin)
