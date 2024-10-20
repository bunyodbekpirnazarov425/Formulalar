from django.urls import path
from .views import AnswerListCreateAPIView, CommentListCreateAPIView, AnswerListCreateAPIView

urlpatterns = [
    path('topics/', AnswerListCreateAPIView.as_view(), name='topic-list-create'),
    path('comments/', CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('replies/', AnswerListCreateAPIView.as_view(), name='reply-list-create'),
]
