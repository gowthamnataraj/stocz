from django.contrib import admin
from .models import Catagory, Item, Vendor, StockLocation, ItemAdmin


admin.site.site_title = 'Venus Knitting'
admin.site.index_title = 'Admin'
admin.site.site_header = 'Venus Knitting'
        
           
admin.site.register(Catagory)
admin.site.register(Item, ItemAdmin)
admin.site.register(Vendor)
admin.site.register(StockLocation)
