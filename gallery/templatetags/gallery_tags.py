from django import template
from gallery.models import Photo

register = template.Library()


@register.inclusion_tag('blog/include/tags/gallery_tags.html')
def get_gallery():
    photos = Photo.objects.order_by()[:5]
    return {"photos": photos}
