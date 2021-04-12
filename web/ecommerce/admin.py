from django.contrib import admin
from .models import ItemInfo


class ItemInfoAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ('item_name', 'item_price',
                    'item_company', 'image_', 'item_stock')
    list_filter = ('item_company', )
    search_fields = ('item_name', )


admin.site.register(ItemInfo, ItemInfoAdmin)
