from django.urls import path
from .views import (
    post_list,
    post_details,
    post_create,    
    signup_view,
    post_update,
    post_detele,
    myposts,
)
from django.contrib.auth import views as auth_views
from .views import CustomPasswordChangeView, password_change_done


urlpatterns = [
    path("", post_list, name="post_list"),
    path("myposts/", myposts, name="myposts"),
    path("post/create/", post_create, name="post_create"),
    path("post/<int:id>", post_details, name="post_details"),
    # path("post/<int:id>/like", like_post, name="like_post"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", signup_view, name="signup"),    
    path("post/update/<int:id>/", post_update, name="post_update"),
    path("post/delete/<int:id>/", post_detele, name="post_delete"),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', password_change_done, name='password_change_done'),
]
