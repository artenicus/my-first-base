from django.shortcuts import render
from django.utils import timezone
from .models import Post
def post_list(request):
    posts = Post.objects.filter(Data_Publikacji__lte=timezone.now()).order_by('Data_Publikacji')
    return render(request, 'blog/post_list.html', {'posts': posts})


# Create your views here.
