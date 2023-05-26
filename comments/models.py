from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from recommendations.models import Recommendation


class Comment(models.Model):
    '''
    Comment model related to User and Post
    '''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        '''
        Orders Comment objects in the order latest to old
        '''
        ordering = ['-created_on']

    def __str__(self):
        '''
        Returns the string representation of a model instance
        '''
        return self.content
