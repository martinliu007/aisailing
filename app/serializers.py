from rest_framework import serializers
from app.models import App
from user_info.serializers import UserDescSerializer


# 父类变成了 ModelSerializer
class ArticleListSerializer(serializers.ModelSerializer):
    articleurl = serializers.HyperlinkedIdentityField(view_name="app:detail")

    author = UserDescSerializer(read_only=True)
    class Meta:
        model = App
        fields = [
            'id',
            'title',
            # 'body',
            'articleurl',
            'created',
            'author'
        ]

class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = '__all__'
