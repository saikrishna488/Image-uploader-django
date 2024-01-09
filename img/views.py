from django.shortcuts import render,HttpResponse as res
from .forms import ImageForm
from .models import Image

def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("saved")
    form = ImageForm()
    img = Image.objects.all()
    return render(request,"home.html",{'form' : form,"img":img})
