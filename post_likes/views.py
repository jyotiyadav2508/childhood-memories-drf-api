from rest_framework import generics, permissions
from childhood_memories_drf_api.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from .models import PostLikes, Post
from .serializers import PostLikesSerializer


class PostLikesList(generics.ListCreateAPIView):
    """
    Class based view to list all post likes
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostLikesSerializer
    queryset = PostLikes.objects.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=serializer.initial_data['post'])
        if post.owner == self.request.user:
            raise PermissionDenied
        else:
            serializer.save(owner=self.request.user)


class PostLikesDetail(generics.RetrieveDestroyAPIView):
    """
    Class based detailed view to retrieve a post like
    Can delete a like if you are the owner
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostLikesSerializer
    queryset = PostLikes.objects.all()
