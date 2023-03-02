from django import forms

from django_select2 import forms as s2forms
from .models import Post, AddMemory, VoluenteerApplication, Comment
from ckeditor.widgets import CKEditorWidget


class PostCreateForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget)
    class Meta:

        model = Post

        fields = [
            'title', 
            'description', 
            'image', 
            'category', 
            'tags', 
            'is_draft',
        ]

        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"}),
            "category": forms.Select(attrs={"class":"form-control"}),
            "tags": forms.SelectMultiple(attrs={"class":"form-control"}), 
            "is_draft": forms.CheckboxInput(attrs={"class":"form-control"}),
        }


class AddOrganizationMemoryForm(forms.ModelForm):
    class Meta:

        model = AddMemory

        fields = [
            'title', 
            'image', 
            'is_draft',
            'organization',

          
        ]

        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"}),
            "is_draft": forms.CheckboxInput(attrs={"class":"form-control"}),
            "organization":forms.Select(attrs={"class":"form-control"}),
        }


class OrgWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "org_name__icontains",
    ]


class VoluenteerApplicationForm(forms.ModelForm):
    
    class Meta:
        model = VoluenteerApplication
        fields = [
            'organization', 
            'first_name',
            'last_name',
            'age',
            'email', 
            'mobile',
            'answer1',
            'answer2'
        ]

        widgets = {
            "organization":forms.Select(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "mobile":forms.TextInput(attrs={"class":"form-control"}) , 
            "answer1":forms.TextInput(attrs={"class":"form-control"}) , 
            "answer2":forms.NumberInput(attrs={"class":"form-control"}) , 
            'first_name': forms.TextInput(attrs={"class":"form-control"}),
            'last_name':forms.TextInput(attrs={"class":"form-control"}),
            'age': forms.NumberInput(attrs={"class":"form-control"}),
            'email': forms.EmailInput(attrs={"class":"form-control"}),
        }





class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            "text":forms.Textarea(attrs={"class":"form-control"})
        }






















