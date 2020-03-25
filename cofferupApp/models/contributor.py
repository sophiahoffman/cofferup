from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from cloudinary.models import CloudinaryField

class Contributor(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image_url = models.URLField(default="", max_length=200)

    # def __str__(self):
    #     return f'{self.user.first_name} {self.user.last_name}'

    # class Meta:
    #     ordering = (F('user.date_joined').asc(nulls_last=True),)

# Every time a `User` is created, a matching `Librarian`
# object will be created and attached as a one-to-one
# property

    @receiver(post_save, sender=User)
    def create_contributor(sender, instance, created, **kwargs):
        if created:
            Contributor.objects.create(user=instance)

# Every time a `User` is saved, its matching `Librarian`
# object will be saved.

    @receiver(post_save, sender=User)
    def save_contributor(sender, instance, **kwargs):
        instance.contributor.save()