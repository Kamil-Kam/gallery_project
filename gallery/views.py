from django.shortcuts import render
from . models import Gallery, Category

# Create your views here.
#
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


def add_photo(request):
    if request.method == "POST":
        data = request.POST['description']
        image = request.FILES.get("image")

        Gallery.objects.create(
            category=Category.objects.get(category_name='Visitors photos'),
            description=data,
            image=image
        )

    return render(request, 'gallery/add_photo.html')


def main_website(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'gallery/main.html', context)


