from django.urls import path
from post_likes import views

urlpatterns = [
    path('post_likes/', views.PostLikesList.as_view()),
    path('post_likes/<int:pk>/', views.PostLikesDetail.as_view())
]
