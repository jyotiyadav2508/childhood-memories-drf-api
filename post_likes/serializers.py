from django.db import IntegrityError
from rest_framework import serializers
from .models import PostLikes


class PostLikesSerializer(serializers.ModelSerializer):
    '''
    Class for PostLikes model serializer
    '''
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = PostLikes
        fields = ['id', 'created_on', 'owner', 'post',]

    def create(self, validated_data):
        '''
        Integrity error check taken from Code Institute's DRF example project.
        Ensures duplicate post likes returns error message to user.
        '''
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                {'detail': 'possible deplication'}
            )
