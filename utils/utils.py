import random
from django.utils.text import slugify


def slugify_instance_product_name(instance, save=False, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.product_name)
    Klass = instance.__class__
    qs = Klass.objects.filter(slug=slug).exclude(id=instance.id)
    rand_int = random.randint(300_000, 500_000)
    if qs.exists():
        slug = f'{slug}-{rand_int}'
        return slugify_instance_product_name(instance, save=save, new_slug=slug)
    instance.slug = slug
    if save:
        instance.save()
    return instance