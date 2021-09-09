from re import U
from django.shortcuts import get_object_or_404, render
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from .serializers import PostSerializer, CommentSerializer, LikeSerializer, ProfileSerializer, RegisterSerializer, ChangePasswordSerializer, UpdateUserSerializer
from .models import Post, Comment, Like
from django.contrib.auth.models import User
from rest_framework.response import Response
import cloudinary.uploader
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken, OutstandingToken, BlacklistedToken



class RegisterView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        register = RegisterSerializer(data=request.data)
        if register.is_valid():
            register.save()
            return Response(register.data, status=status.HTTP_201_CREATED)
        return Response(register.errors, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response({'message': 'Logout was successfully!'}, status=status.HTTP_205_RESET_CONTENT)

class ProfileView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request,):
        user = User.objects.all()
        serializer = ProfileSerializer(user, many=True)
        return Response(serializer.data)
        

class ProfileViewDetail(APIView):
    permission_classes = (AllowAny,)
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = ProfileSerializer(user)
        return Response(serializer.data)


class post_list(APIView):
    def get(self, request, ):
        posts = Post.objects.all()
        body = request.query_params.get('body', None)
        if body is not None:
            posts = posts.filter(body__icontains=body)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


    def post(self, request):
        post = PostSerializer(data=request.data)
        if request.data.get('image'):
            cloudinary.uploader.upload(request.data.get('image'))
        if post.is_valid():
            post.save()
            return Response(post.data, status=status.HTTP_201_CREATED)
        return Response(post.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        post = Post.objects.all()
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class post_detail(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        if request.data.get('image'):
            cloudinary.uploader.upload(request.data.get('image'))
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response({'message': 'Post was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    
class comment_list(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        comment = CommentSerializer(data=request.data)
        if comment.is_valid():
            comment.save()
            return Response(comment.data, status=status.HTTP_201_CREATED)
        return Response(comment.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        comment = Comment.objects.all()
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class comment_detail(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = self.get_object(pk)
        comment.delete()
        return Response({'message': 'Comment was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


class comment_list_author(APIView):
    def get_queryset(self):
        queryset = Comment.objects.all()
        author = self.request.query_params.get('author')
        if author is not None:
            queryset = queryset.filter(author__author=author)
        return queryset


class like_post(APIView):
    def get(self, request):
        likes = Like.objects.all()
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data)

    def post(self, request):
        like = LikeSerializer(data=request.data)
        if like.is_valid():
            like.save()
            return Response(like.data, status=status.HTTP_201_CREATED)
        return Response(like.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        like = Like.objects.all()
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)