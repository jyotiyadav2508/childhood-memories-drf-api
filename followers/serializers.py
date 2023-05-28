from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.timezone import now
from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    '''
    Class for Follower model serializer
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(
        source='followed.username')
    following_length_days = serializers.SerializerMethodField()

    def get_following_length_days(self, obj):
        """
        Serializer method field to get the
        length of days followed in days
        """
        return (now() - obj.created_on).days

    class Meta:
        model = Follower
        fields = ['id', 'created_on', 'following_length_days',
                  'owner', 'followed', 'followed_name'
                  ]

    def create(self, validated_data):
        # Create method handles the unique constraint on 'owner' and 'followed'
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                {'detail': 'possible deplication'}
            )
