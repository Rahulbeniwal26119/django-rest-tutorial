# Create your views here.
from ftplib import ftpcp
from webbrowser import get
from rest_framework.decorators import api_view
from .models import Post
from rest_framework.response import Response 
from rest_framework import status 
from .forms import PostForm
from rest_framework.views import APIView



def get_posts(request):
    user_name = request.GET.get('user_name')
    print("user_name", user_name)
    if user_name:
        user_name= user_name.title()
        try:
            post = Post.objects.get(author=user_name)
            posts = {
                'id': post.id,
                'author': post.author,
                'title': post.title
            }
        except Exception as e:
            posts = Post.objects.all().values()
    else:
        posts = Post.objects.all().values()
    
    # if user_name is given then only give 
    # detail of that user else give all posts
    
    return Response(
        data = posts, 
        status = status.HTTP_200_OK
    )


def create_or_update_post(request):
    try:
        post_id = request.POST.get('id')
        if not post_id:
            form_data = PostForm(request.POST)
            if not form_data.is_valid():
                return Response(
                    data = form_data.errors,
                    status = status.HTTP_400_BAD_REQUEST
                )
            cleaned_data = form_data.cleaned_data

            post = Post.objects.create(
                title = cleaned_data['title'],
                author = cleaned_data['author']
            )

            return Response(
                data = post.id,
                status = status.HTTP_201_CREATED 
            )
        else:
            form_data = PostForm(request.POST)
            if not form_data.is_valid():
                return Response(
                    data = form_data.errors,
                    status = status.HTTP_400_BAD_REQUEST
                )
            cleaned_data = form_data.cleaned_data

            post = Post.objects.filter(id=post_id).update(
                title = cleaned_data['title'],
                author = cleaned_data['author']
            )

            return Response(
                data = post, 
                status = status.HTTP_200_OK
            )
    except Exception as e:
        return Response(
            data = e,
            status = status.HTTP_500_INTERNAL_SERVER_ERROR
        )


def delete_post(request):
    try:
        post_id = request.GET.get('id')
        if not post_id:
            return Response(
                data = 'No post id given',
                status = status.HTTP_400_BAD_REQUEST
            )
        else:
            post = Post.objects.filter(id=post_id).delete()
            return Response(
                data = post,
                status = status.HTTP_200_OK
            )
    except Exception as e:
        return Response(
            data = e,
            status = status.HTTP_500_INTERNAL_SERVER_ERROR
        )


class PostCrudViews(APIView):

    def get(self, request):
        return get_posts(request._request)

    def post(self, request):
        return create_or_update_post(request._request)
    
    def delete(self, request):
        return delete_post(request._request)



@api_view(['GET'])
def get_post_details_paginated(request):

    page_size = int(request.GET.get('page_size') or 5)
    offset = int(request.GET.get("offset") or  1)

    user_name = request.GET.get("user_name")

    filter = {}
    if user_name:
        filter.update({'user': user_name})
    
    post_detail = Post.objects\
        .all(**filter).values().order_by('id')[(offset-1)*page_size: 
        (offset-1)*page_size+page_size]
    
    total_record = Post.objects.filter(**filter).count()

    return Response(
        data = {
            'post_detail': post_detail,
            'total_record': total_record
        },
        status = status.HTTP_200_OK
    )

