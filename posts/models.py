from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    """
    class Category(models.TextChoices):
        '''
        A class for the category key
        Contains different type of cateogry of posts
        '''
        SPORT = 'Sport',
        SCHOOL = 'School',
        BOOKS = 'Books',
        PERSON = 'Person',
        PLACE = 'Place',
        EVENT = 'Event',
        Art = 'Art',
        Media = 'Media',
        OTHERS = 'Others',

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    category = models.CharField(
        max_length=50,
        choices=Category.choices
    )
    image = models.ImageField(
        upload_to='images/', default='../default_post_ppnjua', blank=True
    )

    class Meta:
        '''
        Orders Posts objects in the order latest to old
        '''
        ordering = ['-created_on']

    def __str__(self):
        '''
        Returns the string representation of a model instance
        '''
        return f'{self.id} {self.title}'
