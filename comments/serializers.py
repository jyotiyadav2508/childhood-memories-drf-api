from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime
from .models import Comment
from comment_likes.models import CommentLikes


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    Adds some extra fields when returning a list of Comment instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    created_on = serializers.SerializerMethodField()
    updated_on = serializers.SerializerMethodField()
    comment_likes_id = serializers.SerializerMethodField()
    comment_likes_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    # shows how long ago was the comment created or updated
    def get_created_on(self, obj):
        return naturaltime(obj.created_on)

    def get_updated_on(self, obj):
        return naturaltime(obj.updated_on)

    def get_comment_likes_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            comment_likes = CommentLikes.objects.filter(
                owner=user, comment=obj
            ).first()
            return comment_likes.id if comment_likes else None
        return None

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_on', 'updated_on',
            'post', 'content', 'comment_likes_id', 'comment_likes_count',
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Class for CommentDetailSerializer
    that inherits from the CommentSerializer
    Post is a read only field so that we dont have to set it on each update
    """
    post = serializers.ReadOnlyField(source='post.id')
