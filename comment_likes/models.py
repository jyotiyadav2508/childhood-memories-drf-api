from django.db import models
from django.contrib.auth.models import User
from comments.models import Comment


class CommentLikes(models.Model):
    """
    Class based model for Comment Likes.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''
        Class meta to set the order of comments likes, newest first
        '''
        ordering = ['-created_on']
        unique_together = ['owner', 'comment',]

    def __str__(self):
        """
        Function to create the string for representing Comment Likes model
        in admin.
        """
        return f'{self.owner} liked your comment: {self.comment}'
