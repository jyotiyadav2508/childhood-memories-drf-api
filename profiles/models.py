from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    '''
    Profile model.
    Extends User model with additional information about user
    '''
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # Default profile image
    image = models.ImageField(
        upload_to='images/', default='../default_profile_aje7vu'
    )

    class Meta:
        '''
        Orders Profile objects in reverse order of when they were created
        '''
        ordering = ['-created_on']

    def __str__(self):
        ''' Returns the string representation of a model instance
        (dunder string method)
        '''
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    # Creates a Profile object automatically when a User is created
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
