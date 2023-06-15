from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from childhood_memories_drf_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from django.db.models import Count
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """
    Lists all the created comments
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.annotate(
        comment_likes_count=Count('comment_likes', distinct=True),
    ).order_by('-created_on')
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner',
        'post',
    ]

    def perform_create(self, serializer):
        '''
        Asociates the Comment with the user creating Comment
        '''
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Displays details of selected Comment
    Allows the owner to edit/delete it
    '''
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.annotate(
        comment_likes_count=Count('comment_likes', distinct=True),
    ).order_by('-created_on')
