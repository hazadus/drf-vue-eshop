from django.urls import path

from .views import UserDetailView

urlpatterns = [
    path("user/details/", UserDetailView.as_view()),
]
