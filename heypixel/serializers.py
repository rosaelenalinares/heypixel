from rest_framework import serializers
from .models import Post, Comment, Like, User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password



class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'image', 'bio')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            image=validated_data['image'],
            bio=validated_data['bio']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if user.is_authenticated:
            if not user.check_password(value):
                raise serializers.ValidationError({"old_password": "Old password is not correct"})
            return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'image', 'bio')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    def update(self, instance, validated_data):
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']
        instance.username = validated_data['username']
        instance.image = validated_data['image']
        instance.bio = validated_data['bio']
        instance.save()
        return instance


class PostSerializer(serializers.ModelSerializer):
    # author = serializers.StringRelatedField(many=False)
    # comments = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='body_comment'
    #  )
    class Meta:
        model = Post
        fields = (
            'id', 
            'body', 
            'created_on', 
            'author', 
            'image',
            'comments',
            'likes'
        )

class CommentSerializer(serializers.ModelSerializer):
    # author = serializers.StringRelatedField(many=False)
    # post = serializers.SlugRelatedField(
    #     many=False,
    #     read_only=True,
    #     slug_field='body'
    #  )
    class Meta:
        model = Comment
        fields = (
            'id', 
            'body_comment', 
            'created_on', 
            'post', 
            'author',
        )

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = (
            'id', 
            'like_post',
            'author',
        )


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username', 
            'first_name', 
            'last_name', 
            'email',
            'image',
            'bio',
        )
