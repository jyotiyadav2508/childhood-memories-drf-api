from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Recommendation
from .serializers import RecommendationSerializer
from childhood_memories_drf_api.permissions import IsOwnerOrReadOnly


class RecommendationList(generics.ListCreateAPIView):
    '''
    Lists all the created Recommendations
    '''
    serializer_class = RecommendationSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Recommendation.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_on')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',  # Return user's recommendation
        'likes__owner__profile',  # Return recommendation a specific user liked
        'owner__profile',  # Return recommendation owned by a specific user
        'category',  # Return which category the recommendation belongs to
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_on',
    ]
    search_fields = [
        'content',
        'reason',
        'category',
        'title',
    ]

    def perform_create(self, serializer):
        '''
        Asociates the Recommendation with the user creating Recommendation
        '''
        serializer.save(owner=self.request.user)


class RecommendationDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Displays details of selected Recommendation
    Allows the owner to edit or delete it
    '''
    serializer_class = RecommendationSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Recommendation.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_on')
