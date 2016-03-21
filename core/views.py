from django.shortcuts import render
from core.models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    context = {}
    context['posts'] = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request,'index.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})