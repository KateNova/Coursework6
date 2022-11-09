from rest_framework import serializers

from .models import Ad, Comment
from .validators import MinLengthValidator


class CommentSerializer(serializers.ModelSerializer):
    ad_id = serializers.IntegerField(
        source='ad.id',
        read_only=True,
    )
    author_image = serializers.ImageField(
        source='author.image',
        read_only=True,
    )
    author_id = serializers.CharField(
        source='author.id',
        read_only=True,
    )
    author_first_name = serializers.StringRelatedField(
        source='author.first_name',
        read_only=True,
    )
    author_last_name = serializers.StringRelatedField(
        source='author.last_name',
        read_only=True,
    )
    text = serializers.CharField(
        validators=(
            MinLengthValidator(8),
        )
    )

    class Meta:
        model = Comment
        fields = (
            'pk',
            'text',
            'created_at',
            'author_image',
            'ad_id',
            'author_id',
            'author_first_name',
            'author_last_name',
        )


class AdSerializer(serializers.ModelSerializer):

    title = serializers.CharField(
        validators=(
            MinLengthValidator(8),
        )
    )

    class Meta:
        model = Ad
        fields = (
            'pk',
            'image',
            'title',
            'price',
            'description',
        )


class AdDetailSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(
        source='author.phone',
        read_only=True,
    )
    author_id = serializers.CharField(
        source='author.id',
        read_only=True,
    )
    author_first_name = serializers.StringRelatedField(
        source='author.first_name',
        read_only=True,
    )
    author_last_name = serializers.StringRelatedField(
        source='author.last_name',
        read_only=True,
    )

    class Meta:
        model = Ad
        fields = (
            'pk',
            'image',
            'title',
            'price',
            'description',
            'phone',
            'author_id',
            'author_first_name',
            'author_last_name',

        )
