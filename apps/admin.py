from django.contrib import admin
from .models import Category, Blogs, UserProfile
# Register your models here.
admin.site.register(Category),
admin.site.register(Blogs),
admin.site.register(UserProfile)

class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ("user", "village", "province", "district", "mobile", "picture")
    list_filter = ["user"]
    search_fields = ["user"]