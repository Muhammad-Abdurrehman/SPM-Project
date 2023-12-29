from django.shortcuts import render
from .models import UploadedPicture

def home(request):
    pictures = UploadedPicture.objects.all()
    
    context = {'pictures': pictures}
    return render(request, 'myapp/home.html', context)

