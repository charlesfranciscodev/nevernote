from rest_framework import generics
from .models import CustomUser, Note, Notebook, Tag
from .serializers import UserSerializer, NoteSerializer, NotebookSerializer, TagSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import BasePermission, IsAuthenticated, IsAdminUser


class IsUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user:
            return obj == request.user
        return False


class UserListView(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsUser,)
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
        return Notebook.objects.filter(author=self.request.user)

    def pre_save(self, obj):
        import sys
        obj.user = self.request.user
        print(obj.title, obj.user, file=sys.stderr)


class NotebookDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = NotebookSerializer

    def get_queryset(self):
        """
        This view should return a list of all the notebooks
        for the currently authenticated user.
        """
        return Notebook.objects.filter(author=self.request.user)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class TagListView(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
