from django.shortcuts import render
from dietitian.models import Contact, Blog
import uuid
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def index(request):
    if request.method=="POST":
        em = request.POST['em']
        ps = request.POST['ps']
        user = auth.authenticate(username=em, password=ps)
        if user is not None:
            auth.login(request, user)
            return render(request, 'user-blog.html',{'username':em})
        else:
            return render(request, 'user.html',{'error':em})


    return render(request, 'user.html')

def contact(request):

    data=Contact.objects.all()
    return render(request, 'user-contact.html',{'data':data})

def contact1(request, cid):

    delete = Contact.objects.filter(c_id=cid)
    delete.delete()
    thank=True
    return render(request, 'user-contact.html',{'thank':thank})

def blog(request):
    if request.method=='POST':
        title=request.POST.get('nm', 'title')
        desc=request.POST.get('desc', 'desc')
        img=request.FILES.get('img', 'img')
        def get_file_path(instance, img):

            ext = img.split('.')[-1]
            img = "%s.%s" % (uuid.uuid4(), ext)
        insert=Blog(title=title,desc=desc,img=img)
        insert.save()
        thank=True
        return render(request,'user-blog.html',{'thank':thank})
    data = Blog.objects.all()
    return render(request, 'user-blog.html',{'data':data})

def editblog(request):
    if request.method=="POST":
        nm = request.POST.get('nm')
        id = request.POST.get('bid')
        eimg = request.POST.get('eimg')
        img = request.FILES.get('img',eimg)
        def get_file_path(instance, img):

            ext = img.split('.')[-1]
            img = "%s.%s" % (uuid.uuid4(), ext)
        desc = request.POST.get('desc')
        edit = Blog.objects.get(b_id=id)
        edit.title=nm
        edit.desc=desc
        edit.img=img
        edit.save()
        done=True
        return render(request,'user-blog.html',{'done':done})

def signup(request):
    if request.method =="POST":
        nm = request.POST.get('nm')
        no = request.POST.get('em')
        ps = request.POST.get('ps')
        cps = request.POST.get('cps')
        if ps == cps:
            insert=User(first_name=nm,username=no,password=ps)
            insert.save()
            auth.login(request,user)
            return render(request,'sign.html',{'error':'New user create'})
        else:
            return render(request,'sign.html',{'error':'password not match'})

    else:

         return render(request,'sign.html')
