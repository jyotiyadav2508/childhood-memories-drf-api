from django.db import IntegrityError
from rest_framework import serializers
from post_likes.models import PostLikes


class PostLikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = PostLikes
        fields = ['id', 'created_on', 'owner', 'post']

    def create(self, validated_data):
        '''
        Handles duplicated likes by the same user
        '''
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplication'})
