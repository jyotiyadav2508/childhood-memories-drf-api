from django.db import IntegrityError
from rest_framework import serializers
from .models import CommentLikes


class CommentLikesSerializer(serializers.ModelSerializer):
    '''
    Class for CommentLikes model serializer
    '''
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = CommentLikes
        fields = ['id', 'created_on', 'owner', 'comment']

    def create(self, validated_data):
        '''
        Integrity error check taken from Code Institute's DRF example project.
        Ensures duplicate comment likes returns error message to user.
        '''
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                {'detail': 'possible duplication'}
            )
