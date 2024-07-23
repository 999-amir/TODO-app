from django.db.models.signals import post_save
from .models import CostumeUser, ProfileModel
from django.dispatch import receiver

@receiver(post_save, sender=CostumeUser)
def create_profile(sender, **kwargs):
    user = kwargs['instance']
    if kwargs['created']:
        ProfileModel.objects.create(user=user)
