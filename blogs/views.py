from django.shortcuts import render
from .models import *
# Create your views here.
def blog(request):

    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        image = request.FILES['image']

        blogs = Blogs(title=title,desc=desc,image=image)
        blogs.save();
        print("saved")

    blog = Blogs.objects.all()
    users = User.objects.all()

    return render(request, 'blog.html',{'blog':blog,'users':users})