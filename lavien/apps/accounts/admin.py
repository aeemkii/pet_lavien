from django.contrib import admin

# Register your models here.
from apps.accounts.models import SocialNetworks, User

@admin.register(SocialNetworks)
class SocialNetworksAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}
    list_display = ["name", "slug","id"]

    

admin.site.register(User)