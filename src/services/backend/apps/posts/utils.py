from django.utils.text import slugify

def post_slug(instance, save=False):
    slug = slugify(instance.title)
    DefaultClass = instance.__class__
    qs = DefaultClass.objects.filter(slug=slug).exclude(id=instance.id)
    slug = f"{slug}"
    instance.slug = slug
    if save:
        instance.save()
    return instance
