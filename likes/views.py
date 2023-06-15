from rest_framework import generics, permissions
from childhood_memories_drf_api.permissions import IsOwnerOrReadOnly
from likes.models import Like, Post
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from likes.serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    """
    List likes or create a like if logged in
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=serializer.initial_data['post'])
        if post.owner == self.request.user:
            raise PermissionDenied
        else:
            serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    '''
    Class for the LikeDetail generic API view
    Retrieve a like or delete it by id if you own it.
    '''
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
