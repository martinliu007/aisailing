from rest_framework import serializers
from app.models import App

# 父类变成了 ModelSerializer
class ArticleListSerializer(serializers.ModelSerializer):
    articleurl = serializers.HyperlinkedIdentityField(view_name="app:detail")

    class Meta:
        model = App
        fields = [
            'id',
            'title',
            'body',
            'articleurl',
            'created',
        ]
        read_only_fields = ['author']

class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = '__all__'
