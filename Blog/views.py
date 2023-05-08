from django.shortcuts import render
from .models import blog
# Create your views here.
def Blog(request):
    post=blog.objects.all()
    # name, value
    return render(request,'Blog/Blog.html',{'post':post})

