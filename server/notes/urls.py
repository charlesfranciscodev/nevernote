from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from notes import views


urlpatterns = [
    path('users/', views.UserListView.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration', include('rest_auth.registration.urls'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
