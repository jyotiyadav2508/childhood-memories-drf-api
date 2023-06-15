from django.urls import path
from post_likes import views

urlpatterns = [
    path('post_likes/', views.PostLikeList.as_view()),
    path('post_likes/<int:pk>/', views.PostLikeDetail.as_view()),
]
