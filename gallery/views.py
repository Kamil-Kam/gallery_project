import time
from django.shortcuts import render
from . models import Gallery, Category

# Create your views here.

# wishlist = Gallery.objects.filter(category__category_name='Visitors photos')
# wishlist.delete()


def gallery(request, category_name):
    images = Gallery.objects.filter(category__category_name=category_name)
    category = Category.objects.get(category_name=category_name)

    context = {
        'images': images,
        'category': category,
    }
    return render(request, 'gallery/gallery.html', context)


def photo(request, category, pk):
    images = Gallery.objects.get(id=pk)
    all_images = Gallery.objects.filter(category__category_name=category)

    context = {
        'images': images,
        'category': category,
        'all_images': all_images,
    }
    return render(request, 'gallery/photo.html', context)


uploaded_ip_list = []


def manage_uploaded_ip(address_ip: str, uploaded_time: float) -> bool:
    ip_count = 0

    for uploaded_ip in uploaded_ip_list:

        if uploaded_time - uploaded_ip[1] > 60:
            uploaded_ip_list.remove(uploaded_ip)

    for uploaded_ip in uploaded_ip_list:
        if uploaded_ip[0] == address_ip:
            ip_count += 1

    if ip_count <= 2:
        uploaded_ip_list.append([address_ip, uploaded_time])

    return True if ip_count <= 2 else False


def add_photo(request):
    uploaded = False
    success = True
    message = 'None'

    if request.method == "POST":

        address_ip = request.META.get('REMOTE_ADDR')
        uploaded_time = time.time()

        if not manage_uploaded_ip(address_ip, uploaded_time):
            uploaded = True
            success = False
            message = 'You can upload only 3 images within 2 minutes. Please wait a moment. '

        else:
            uploaded = True
            message = 'Photo uploaded successfully!'
            data = request.POST['description']
            image = request.FILES.get("image")

            Gallery.objects.create(
                category=Category.objects.get(category_name='Visitors photos'),
                description=data,
                image=image
            )

    context = {
        'uploaded': uploaded,
        'message': message,
        'success': success
    }

    return render(request, 'gallery/add_photo.html', context)


def main_website(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'gallery/main.html', context)


