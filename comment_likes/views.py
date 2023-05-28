from rest_framework import generics, permissions
from childhood_memories_drf_api.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from .models import CommentLikes, Comment
from .serializers import CommentLikesSerializer


class CommentLikesList(generics.ListCreateAPIView):
    """
    Class based view to list all comment likes
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentLikesSerializer
    queryset = CommentLikes.objects.all()

    def perform_create(self, serializer):
        comment = get_object_or_404(
            Comment, pk=serializer.initial_data['comment'])
        if comment.owner == self.request.user:
            raise PermissionDenied
        else:
            serializer.save(owner=self.request.user)


class CommentLikesDetail(generics.RetrieveDestroyAPIView):
    """
    Class based detailed view to retrieve a comment like
    Can delete a like if you are the owner
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentLikesSerializer
    queryset = CommentLikes.objects.all()
