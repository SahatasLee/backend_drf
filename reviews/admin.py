from email.headerregistry import Group
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *


admin.site.register(Category)
admin.site.register(Company)
admin.site.register(ProductSite)
admin.site.register(ProductSize)
admin.site.register(Comment)

admin.site.unregister(Group)

# title name page admin
admin.site.site_header = "Product Review Admin"

# admin.site.register(Product)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'content')
    list_filter = ('category', )