from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class PostLikes(models.Model):
    """
    PostLike model, related to 'owner' which is a User instance and
    'post' which is a Post instance
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        Post,
        related_name="post_likes",
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )

    class Meta:
        """
        Orders Like objects in the order latest to old
        'unique_together' makes sure a user can't like the same post twice
        """

        ordering = ["-created_on"]
        unique_together = ["owner", "post"]

    def __str__(self):
        """
        Returns the string representation of a model instance
        """
        return f"{self.owner} liked your post: {self.post}"
