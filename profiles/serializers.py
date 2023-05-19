from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    ''' Serializer for Profile Model data '''
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_on', 'updated_on', 'name',
            'bio', 'image', 'location',
        ]
