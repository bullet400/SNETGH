from django.contrib import admin
from django.contrib.auth.models import Group
from accounts.models import Product, Customer, Order, Tag
# Register your models here.

class AdminCustomer(admin.ModelAdmin):
    list_display =('title','first_name','last_name', 'email','phone')
    search_fields =('first_name','last_name','email','phone')
    date_hierarchy ='date_created'

class AdminProduct(admin.ModelAdmin):
    list_display =('product_name','price','category','description')
    #list_editable =['product_name']
    list_display_links =('category',)
    date_hierarchy ='date_created'


admin.site.register(Order)
admin.site.register(Product,AdminProduct)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Tag)
#admin.site.unregister(Group)