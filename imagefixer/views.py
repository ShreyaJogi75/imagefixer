from django.shortcuts import render
from django.http import JsonResponse
from PIL import Image, ImageEnhance
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import os

def home(request):
    return render(request, 'index.html')

def services(request):
    edited_image_data = request.session.get('croppedImageData', None)
    context = {'edited_image_data': edited_image_data}
    return render(request, 'services.html', context)
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def home(request):
    return render(request, 'index.html') 

def edit_image(request):
    return render(request, 'edit_image.html')

def adjust_brightness_contrast(image, brightness_factor, contrast_factor):
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness_factor)
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(contrast_factor)
    return image

def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        uploaded_image = request.FILES['image']
        
        # Open the uploaded image using Pillow
        image = Image.open(uploaded_image)
        
        # Adjust brightness and contrast
        brightness_factor = 1.5  # Example brightness factor
        contrast_factor = 1.2    # Example contrast factor
        image = adjust_brightness_contrast(image, brightness_factor, contrast_factor)
        
        # Convert image back to bytes
        output = BytesIO()
        image.save(output, format='JPEG')
        output.seek(0)
        
        # Prepare the adjusted image to be saved
        adjusted_image = InMemoryUploadedFile(
            output,
            'ImageField',
            f"{uploaded_image.name.split('.')[0]}_adjusted.jpg",
            'image/jpeg',
            output.tell(),
            None
        )
        
        # Add adjusted image to session for later use (optional)
        request.session['adjusted_image'] = adjusted_image
        
        # Now you can use 'adjusted_image' to save or display the adjusted image
        
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
