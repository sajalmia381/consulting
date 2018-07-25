from django.urls import path
from .views import BlogList, BlogDetails, ParentCommentView, parent_comment, child_comment

app_name = 'blog'
urlpatterns = [
    path('', BlogList.as_view(), name='blog_list'),
    path('<pk>/', BlogDetails.as_view(), name='blog_detail'),
    path('comment', ParentCommentView.as_view(), name='comment'),
    path('<pk>/parent-comment', parent_comment, name='parent_comment'),
    path('<blog_pk>/parent-comment/<comment_pk>/child-comment', child_comment, name='child_comment'),
]