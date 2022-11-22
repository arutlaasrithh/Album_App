from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ImageForm
from .models import Image

# Create your views here.
def upload(request):
 if request.method == "POST":
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
     form.save()
 form = ImageForm()
 img = Image.objects.all().order_by('-id')
 return render(request, 'photo/upload.html', {'img':img, 'form':form})
# return render(request, "photo/home.html")

def home(request):
    return render(request, 'photo/home.html')

def about(request):
    return render(request, 'photo/about.html')

def gallery(request):
    search_query = request.GET.get('search','')
    if search_query:
        img = Image.objects.filter(name__icontains=search_query)
    else:
        img = Image.objects.all().order_by('id')
    return render(request, 'photo/gallery.html', {'img':img})

def delete_image(request,pk):
    if request.method == 'POST':
        imgd = Image.objects.get(pk=pk)
        imgd.delete()
    return redirect('gallery')

def update(request):
    img = Image.objects.all().order_by('id')
    return render(request, 'photo/update.html', {'img':img})

def update_image(request,pk):
    photo = Image.objects.get(pk=pk)
    form = ImageForm(request.POST or None, request.FILES or None, instance=photo)
    if request.method == "POST":
      if form.is_valid():
       form.save() 
       return redirect('gallery')
    return render(request, 'photo/update_image.html', {'photo':photo, 'form':form})


    



