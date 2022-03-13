from django.contrib import admin
from product.models import Product, Review, Photo

admin.site.register(Review)


class InlineProductImage(admin.TabularInline):
    model = Photo


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'p_name', 'p_category', 'p_soldOut']
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        for img in request.FILES.getlist('photos'):
            obj.photo_set.create(image=img)

admin.site.register(Product, ProductAdmin)
