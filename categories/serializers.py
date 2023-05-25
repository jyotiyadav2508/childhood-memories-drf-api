from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model
    """
    name = serializers.CharField(source='category', read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'id', 'created_on', 'updated_on']
