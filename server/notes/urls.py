from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from notes import views


urlpatterns = [
    path('users/', views.UserListView.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration', include('rest_auth.registration.urls')),
    path('notebooks/', views.NotebookListCreateView.as_view()),
    path('notebooks/<int:pk>/', views.NotebookDetail.as_view()),
    path('notes/', views.NoteCreateView.as_view()),
    path('notes/<int:pk>/', views.NoteDetail.as_view()),
    path('tags/', views.TagListCreateView.as_view()),
    path('tags/<int:pk>/', views.TagDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
