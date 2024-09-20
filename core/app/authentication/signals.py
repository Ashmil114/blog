from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import tb_user
from .models import CustomUser


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        tb_user.objects.create(user=instance)


# @receiver(post_save, sender=CustomUser)
# def save_user_profile(sender, instance, **kwargs):
#     instance.user.save()
