from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def display_carousel(all_images, images):
    match = False
    carousel_items = ''

    for image in all_images:
        if image.id == images.id:
            match = True

        if match:
            if image.id != images.id:
                carousel_items += f'<div class="carousel-item"><a href="http://127.0.0.1:8000{image.image.url}"><img src="{image.image.url}" ' \
                                  f'class="center rounded" alt="image not found"></a><p class="text-center py-3">{image.description}</p></div>'

    for image in all_images:
        if image.id == images.id:
            match = False

        if match:
            carousel_items += f'<div class="carousel-item"><a href="http://127.0.0.1:8000{image.image.url}"><img src="{image.image.url}" ' \
                              f'class="center rounded" alt="image not found"></a><p class="text-center py-3">{image.description}</p></div>'

    return mark_safe(carousel_items)
