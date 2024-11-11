# blog/forms.py
from django import forms
from .models import Post, Tag
from tinymce.widgets import TinyMCE 

class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCE(
            attrs={'cols': 80, 'rows': 30},
            mce_attrs={
                'plugins': 'link image media code table',
                'toolbar': 'undo redo | bold italic | alignleft aligncenter alignright | bullist numlist | link image media | code | table',
                'menubar': 'file edit view insert format tools table',
                'file_picker_types': 'image',  
                'image_caption': True 
            }
        )
    )
    slug = forms.SlugField(max_length=200, required=True, label="Slug")
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,  
        label="Etiketler" 
    )

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content','slug','status','tags']
