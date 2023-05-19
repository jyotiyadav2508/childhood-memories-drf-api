from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(APIView):
    '''
    Lists all the profiles
    No create view required since profile creation is handled by
    Django signals.
    '''
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
