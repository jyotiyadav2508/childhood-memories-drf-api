from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Category
from .serializers import CategorySerializer


class CategoriesList(generics.ListCreateAPIView):
    """
    Categories list view
    """
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()


class CategoriesDetail(generics.RetrieveAPIView):
    """
    Categories detailed view.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
