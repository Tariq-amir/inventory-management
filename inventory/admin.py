from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display=('tender_no', 'name','model','price','date_of_buy','month_year','year','alloted','room')

admin.site.register(Product,ProductAdmin)