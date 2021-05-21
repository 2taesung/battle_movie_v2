from rest_framework import serializers
from .models import Community, Movie

class CommunitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Community
        fields = (
            'title', 'overview', 'poster_path',
            # 'created_at', 'updated_at',
        )