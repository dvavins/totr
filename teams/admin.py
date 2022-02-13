from django.contrib import admin

from teams.models import Teams, Members, TodosGroup, TranxGroup


class MemberInline(admin.StackedInline):
    model = Members
    extra = 0


class TeamsAdmin(admin.ModelAdmin):

    readonly_fields = ['slug']
    inlines = [MemberInline]


admin.site.register(Teams, TeamsAdmin)
admin.site.register(Members)
admin.site.register(TodosGroup)
admin.site.register(TranxGroup)
