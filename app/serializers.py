from rest_framework import serializers
from .models import Subject, Comment, Answer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'comment', 'reply_text', 'created_by', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'topic', 'comment_text', 'created_by', 'created_at', 'replies']

class SubjectSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Subject
        fields = ['id', 'title', 'description', 'created_by', 'created_at', 'comments']
