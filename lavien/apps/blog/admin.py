from django.contrib import admin
from django import forms

from ckeditor.widgets import CKEditorWidget


# Register your models here.
from apps.blog.models import Category, Post, Organization, Tag, AddMemory, VoluenteerApplication, Comment

class PostAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = '__all__'





@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ["title", "category","created", "is_draft",]
    list_filter = ["category", "is_draft", "created"]
    # filter_horizontal = ["tags"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}
    list_display = ["name", "slug","id"]


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("org_name",)}
    list_display = ["org_name", "slug","id"]

    

@admin.register(AddMemory)
class AddMemoryAdmin(admin.ModelAdmin):
    list_display = ["created"]



@admin.register(VoluenteerApplication)
class VoluenteerApplicationAdmin(admin.ModelAdmin):
    list_display = [
        "organization",
        "email",
        "first_name",
        "last_name",
        "created"
        ]

@admin.register(Comment)
class CommmentAdmin(admin.ModelAdmin):
    list_display = ["created", "author", "text"]

