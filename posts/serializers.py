from rest_framework import serializers
from posts.models import Post
from post_likes.models import PostLikes


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    post_likes_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comment_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_post_likes_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            post_likes = PostLikes.objects.filter(
                owner=user, post=obj
            ).first()
            return post_likes.id if post_likes else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_on', 'updated_on',
            'title', 'content', 'image', 'category', 'post_likes_id',
            'likes_count', 'comment_count',
        ]
