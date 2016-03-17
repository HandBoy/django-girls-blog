from django.shortcuts import render
from core.models import Post
# Create your views here.
def index(request):
    context = {}
    context['posts'] = Post.objects.all()
    return render(request,'index.html', context)