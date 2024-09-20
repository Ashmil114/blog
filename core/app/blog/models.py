from django.db import models
from app.authentication.models import tb_user
import uuid
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver


def image_path(instance, filename):
    _, extension = os.path.splitext(filename)
    return f"post/{instance.id}{extension}"


class tb_post(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    title = models.TextField(blank=False)
    image = models.ImageField(
        upload_to=image_path,
        blank=True,
        null=True,
    )
    description = models.TextField(blank=False)
    owner = models.ForeignKey(
        tb_user, on_delete=models.PROTECT, related_name="posts"
    )  # noqa
    created = models.DateTimeField(auto_now_add=True)
    no_of_views = models.IntegerField(default=0)
    category = models.ForeignKey(
        "tb_category", on_delete=models.PROTECT, related_name="posts"
    )

    def __str__(self) -> str:
        return self.title


@receiver(post_delete, sender=tb_post)
def delete_tb_post_image_file(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)


class tb_category(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    title = models.TextField(blank=False)

    def __str__(self):
        return self.title
