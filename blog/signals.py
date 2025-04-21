from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from .models import Article

@receiver(pre_save, sender=Article)
def generate_or_update_slug(sender, instance, **kwargs):
    if instance.pk:
        old = Article.objects.get(pk=instance.pk)
        if old.title != instance.title:
            # Regenerate slug if title changed
            base_slug = slugify(f"{instance.title}-{instance.created.strftime('%Y%m%d%H%M%S')}-{instance.category}")
        else:
            return # do not change slug if title didn't change
        
    else:
        # It's a new article
        base_slug = slugify(f"{instance.title}-{instance.created.strftime('%Y%m%d%H%M%S') if instance.created else ''}-{instance.category}")

    unique_slug = base_slug
    counter = 1

    while Article.objects.filter(slug=unique_slug).exclude(pk=instance.pk).exists():
        unique_slug = f"{base_slug}-{counter}"
        counter += 1

    instance.slug = unique_slug

