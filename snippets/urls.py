from django.urls import path 
from snippets import views
from rest_framework.urlpatterns \
    import format_suffix_patterns

format_suffix_views = [
    path('snippets/all/', views.all_snippets_list),
] 
urlpatterns = [
    path('snippets/', views.snippets_list),
    path('snippet/<int:pk>/', views.snippets_detail),
    path('name/<int:pk>/', views.get_param),
    path('snippets/class/<int:pk>/', views.SnippetDetail.as_view(), 
    name="get_snippets_detail_class"),
    *format_suffix_views
]

urlpatterns = urlpatterns + format_suffix_patterns(format_suffix_views)