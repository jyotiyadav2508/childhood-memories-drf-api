from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class PostLikes(models.Model):
    """
    Class based model for Post Likes.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name="post_likes", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Class meta to set the order of post likes, newest first
        """

        ordering = ["-created_on"]
        unique_together = ["owner", "post"]

    def __str__(self):
        """
        Function to create the string for representing Post Likes model
        in admin.
        """
        return f"{self.owner} liked {self.post}"
