from django.urls import path
from comment_likes import views

urlpatterns = [
    path('comment_likes/', views.CommentLikesList.as_view()),
    path('comment_likes/<int:pk>/', views.CommentLikesDetail.as_view())
]
