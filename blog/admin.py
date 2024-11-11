import html
from bs4 import BeautifulSoup 
from django.utils.html import format_html, strip_tags
from django.contrib import admin
from .models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_image_tag', 'content_summary')
    list_filter = ['status']
    prepopulated_fields = {"slug": ("title",)}


    def content_image_tag(self, obj):
        soup = BeautifulSoup(obj.content, 'html.parser')
        first_image = soup.find('img')
        
        if first_image and 'src' in first_image.attrs:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', first_image['src'])
        return "No Image"
    
    content_image_tag.short_description = 'Tanıtım Resmi'

    def content_summary(self, obj):
        obj.content= strip_tags(obj.content) #html etiketleri gizler.
        obj.content= html.unescape(obj.content) #html etiketleri gizler.
        return obj.content[:250] + '...' if len(obj.content) > 250 else obj.content
    
    content_summary.short_description = 'İçerik' 

    
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)