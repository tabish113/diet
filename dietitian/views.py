from django.shortcuts import render
from .models import Contact, Blog
import uuid
# Create your views here.
def index(request):
    if request.method=='POST':
        nm=request.POST.get('nm','null')
        em=request.POST.get('em','null')
        no=request.POST.get('no','null')
        msg=request.POST.get('msg','null')
        insert=Contact(nm=nm,em=em,no=no,msg=msg)
        insert.save()
        thank=True
        return render(request, 'index.html',{'thank':thank})

    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def consult(request):
    return render(request, 'consult.html')

def admin1(request):
    if request.method=='POST':
        title=request.POST.get('title', 'title')
        desc=request.POST.get('desc', 'desc')
        img=request.FILES.get('img', 'img')
        def get_file_path(instance, img):

            ext = img.split('.')[-1]
            img = "%s.%s" % (uuid.uuid4(), ext)
        insert=Blog(title=title,desc=desc,img=img)
        insert.save()
        thank=True
        return render(request, 'ad.html',{'thank':thank})

    return render(request, 'ad.html')
