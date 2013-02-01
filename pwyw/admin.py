from django.contrib import admin

from .models import SplitTemplate, UserSplit

#class SplitItemTemplateAdmin(admin.TabularInline):
#    model = SplitItemTemplate

class SplitTemplateAdmin(admin.ModelAdmin):
    model = SplitTemplate
    inlines = (
#        SplitItemTemplateAdmin,
        )

#class UserSplitItemAdmin(admin.TabularInline):
#    model = UserSplitItem
    
class UserSplitAdmin(admin.ModelAdmin):
    model = UserSplit
#    inlines = (
#        UserSplitItemAdmin,
#    )

    list_display = ('user', 'template', 'created_on', 'amount')


admin.site.register(SplitTemplate, SplitTemplateAdmin)
admin.site.register(UserSplit, UserSplitAdmin)
