from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin

class RecipeInline(admin.StackedInline):
    model = models.Recipe
    extra = 1
    
    
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "author", "create_at", "id"]
    inlines = [RecipeInline]
    
@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["name", "prep_time", "cooc_time", "post"]


admin.site.register(models.Category,MPTTModelAdmin)
admin.site.register(models.Comment)

admin.site.register(models.Tag)