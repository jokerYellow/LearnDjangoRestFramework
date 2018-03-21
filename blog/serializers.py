from rest_framework import serializers
from blog.models import Article

class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True,max_length=30)
    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.save()
        return instance

class AArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id','title')