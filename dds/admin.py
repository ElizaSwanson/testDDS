from django.contrib import admin

from .models import Category, FlowType, MoneyFlow, Status, SubCategory

admin.site.register(Status)
admin.site.register(FlowType)
admin.site.register(Category)
admin.site.register(SubCategory)


@admin.register(MoneyFlow)
class FlowAdmin(admin.ModelAdmin):
    list_filter = ("date", "status", "flow_type", "category", "subcategory")
    search_fields = (
        "comment",
        "date",
    )
