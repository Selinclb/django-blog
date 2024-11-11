from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from .models import Post, Tag
from .forms import PostForm
import bleach
from django.views.generic import ListView
from django.http import HttpResponseForbidden

def home(request):
    posts = Pposts = Post.objects.filter(status='published').order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

def index(request):
    posts = Pposts = Post.objects.filter(status='published').order_by('-created_at')
    return render(request, 'blog/index.html', {'posts': posts})

#post listeleme
def post_list(request):
    posts = Pposts = Post.objects.filter(status='published').order_by('-created_at') 
    tags = Tag.objects.all() 
    return render(request, 'blog/post_list.html', {'posts': posts, 'tags':tags})

#post detayları
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)  
    return render(request, 'blog/post_detail.html', {'post': post})

#yeni post ekleme
def post_new(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("Bu sayfaya erişiminiz yok.")
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.content = bleach.clean(post.content, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES)
            post.save()
            form.save_m2m()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

#post düzenleme
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.content = bleach.clean(post.content, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES)
            post.save()
            form.save_m2m() 
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

#blog yazısı silme
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


#tag
class TaggedPostsView(View):
    def get(self, request, tag_id):
        tag = get_object_or_404(Tag, id=tag_id)
        posts = tag.posts.filter(status='published')
        return render(request, 'blog/tagged_posts.html', {'tag': tag, 'posts': posts})

#tagged_posts.html
def tagged_posts(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    posts = Post.objects.filter(tags=tag)
    return render(request, 'blog/tagged_posts.html', {'tag': tag, 'posts': posts})

# İzin verilecek etiketler ve öznitelikler
ALLOWED_TAGS = ['p', 'h2', 'a', 'img', 'strong', 'em', 'ul', 'li']
ALLOWED_ATTRIBUTES = {
    'a': ['href', 'title'],
    'img': ['src', 'alt', 'width', 'height']
}
Post.content = bleach.clean(
    str(Post.content),  # İçeriği metin olarak getir
    tags=ALLOWED_TAGS,
    attributes=ALLOWED_ATTRIBUTES,
)
