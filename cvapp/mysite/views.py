
from django.shortcuts import render
from .forms import UserForm
from django.core.files.storage import FileSystemStorage


# Create your views here.
def index (request):
    form = UserForm()
    if request.method == 'POST':
        form=UserForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = UserForm()
            upload = request.FILES['upload']
            fss = FileSystemStorage()
            file = fss.save(upload.name, upload)
            file_url = fss.url(file)

        else: 
            form= UserForm()
            
    context= {'form':form}
    return render (request,'mysite/navbar.html',context)


    

    
