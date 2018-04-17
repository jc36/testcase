from rest_framework import serializers

from tcase import services
from ..models import Like, Post, User


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = (
            'url',
            'liker',
            'post',
            'like'
        )


class PostSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'url',
            'author',
            'text',
            'created_at',
            'updated_at',
            'is_fan'
        )

    def get_is_fan(self, obj) -> bool:
        """Проверяет, лайкнул ли `request.user` твит (`obj`).
        """
        user = self.context.get('request').user
        return services.is_fan(user, obj)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'url',
            'username',
            'password',
            'email',
            'is_staff'
        )

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
