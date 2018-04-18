from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from tcase import services
from ..models import Like, Post, User


class LikeSerializer(serializers.ModelSerializer):
    liker = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Like
        fields = (
            'url',
            'liker',
            'post',
            'like'
        )


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # is_fan = serializers.Serialize    rMethodField()

    class Meta:
        model = Post
        fields = (
            'url',
            'pk',
            'author',
            'text',
            # 'created_at',
            # 'updated_at',
            # 'is_fan'
        )

    # def get_is_fan(self, obj) -> bool:
    #     """Проверяет, лайкнул ли `request.user` твит (`obj`).
    #     """
    #     user = self.context.get('request').user
    #     return services.is_fan(user, obj)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'url',
            'username',
            'password',
            'email',
            # 'is_staff'
        )

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
