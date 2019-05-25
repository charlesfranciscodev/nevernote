from rest_framework import generics
from .models import CustomUser, Note, Notebook, Tag
from .serializers import UserSerializer, NoteSerializer, NotebookSerializer, TagSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import BasePermission, IsAuthenticated, IsAdminUser


class IsSameUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user:
            return obj == request.user
        return False


class IsOwner(BasePermission):
    """ Checks that the note's notebook belongs to the current user."""
    def has_object_permission(self, request, view, obj):
        if request.user:
            return obj.notebook.user == request.user
        return False


class UserListView(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsSameUser,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class NotebookListCreateView(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = NotebookSerializer

    def get_queryset(self):
        """
        This view should return a list of all the notebooks
        for the currently authenticated user.
        """
        return Notebook.objects.filter(user=self.request.user)

    def pre_save(self, obj):
        obj.user = self.request.user


class NotebookDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = NotebookSerializer

    def get_queryset(self):
        """
        This view should return a list of all the notebooks
        for the currently authenticated user.
        """
        return Notebook.objects.filter(user=self.request.user)


class NoteCreateView(generics.CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsOwner,)
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsOwner,)
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class TagListCreateView(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = TagSerializer

    def get_queryset(self):
        """
        This view should return a list of all the notebooks
        for the currently authenticated user.
        """
        return Tag.objects.filter(user=self.request.user)

    def pre_save(self, obj):
        obj.user = self.request.user


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = TagSerializer

    def get_queryset(self):
        """
        This view should return a list of all the notebooks
        for the currently authenticated user.
        """
        return Tag.objects.filter(user=self.request.user)
