from django.urls import path
from .views import RegisterView, LoginView, ProfileView, UserDeleteView, UserListView, UserRoleUpdateView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),

    path('profile/',ProfileView.as_view(), name='profile' ),
    path('users/',UserListView.as_view(), name='user-list' ),
    path('<int:user_id>/role/',UserRoleUpdateView.as_view(), name='update-role' ),
    path('<int:user_id>/delete/',UserDeleteView.as_view(), name='delete-user' ),

]