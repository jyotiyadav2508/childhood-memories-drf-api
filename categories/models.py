from django.db import models


class Category(models.Model):
    """
    Model for posts categories
    """
    category = models.CharField(max_length=60, unique=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'Category : {self.category}'
