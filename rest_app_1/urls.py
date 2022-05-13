from django.urls import path 
from .views import get_posts, \
    create_or_update_post, delete_post, \
        PostCrudViews, get_post_details_paginated

urlpatterns = [
    path('post-list/', get_posts, name="get_post"),
    path('create-or-update-post/', create_or_update_post, name="create_or_update_post"),
    path('delete-post/', delete_post, name="delete-post"),
    path("post-views/", PostCrudViews.as_view(),
    name="post_crud_views"),
    path("paginated-post-views/",
    get_post_details_paginated, name="paginated_post_views"),
]