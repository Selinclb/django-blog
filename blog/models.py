from django.db import models
from django.db.models import Model
from tinymce.models import HTMLField
from django.utils.text import slugify

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Etiket'
        verbose_name_plural='Etiketler'

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()
    image = models.ImageField(upload_to='images/', blank=True, null=True) 
    slug=models.SlugField(null=False, unique=True)
    status = models.CharField(max_length=20, choices=[('draft', 'Taslak'), ('published', 'Yayınlanan')], default='published')
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name='Yazı'
        verbose_name_plural='Yazılar'
        

    