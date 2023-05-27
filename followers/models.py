from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    '''
    Class for the Follower model.
    'owner_following' is a User who is following another User.
    'followed' is a User who is followed by the 'owner'.
    The related_name attribute differentiates 'owner' and 'followed'
    who both are User model instances.
    '''
    owner = models.ForeignKey(
        User, related_name='following',  on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        # 'unique_together' avoids duplicates
        ordering = ['created_on']
        unique_together = ['owner', 'followed']

    def __str__(self):
        """
        Function to create the string for representing Follower model in admin.
        """
        return f'{self.owner} is following {self.followed}'
