from django.shortcuts import render
from django.http import JsonResponse
from PIL import Image
from django.conf import settings

def home(request):
    return render(request, 'index.html')
def services(request):
    return render(request, 'services.html')
def edit_image(request):
    return render(request, 'edit_image.html')

def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        # Process the uploaded image here
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
def services(request):
    edited_image_data = request.session.get('croppedImageData', None)
    context = {'edited_image_data': edited_image_data}
    return render(request, 'services.html', context)

