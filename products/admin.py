from django.contrib import admin
from .models import Product, Category, Size, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'is_available',
    )

    list_filter = ('category', 'is_available',)
    search_fields = ('name', 'description',)
    filter_horizontal = ('sizes',)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'sizes':
            kwargs['queryset'] = Size.objects.order_by('name')
        return super().formfield_for_manytomany(db_field, request, **kwargs)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )


class SizeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'rating',
        'created_at',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Review, ReviewAdmin)
