from rest_framework import serializers
from .models import CustomUser, Note, Notebook, Tag


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "first_name", "last_name", "profile_photo_url")


class TagSerializer(serializers.ModelSerializer):
    notes = serializers.PrimaryKeyRelatedField(
        queryset=Note.objects.all(), many=True
    )
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Tag
        fields = ("id", "name", "notes", "user")


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ("id", "title", "content", "creation_date_time", "last_updated_date_time", "favorite", "notebook", "tags")
        read_only_fields = ("creation_date_time", "last_updated_date_time")


class NotebookSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    notes = NoteSerializer(many=True, read_only=True)
    
    class Meta:
        model = Notebook
        fields = ("id", "title", "user", "notes")
