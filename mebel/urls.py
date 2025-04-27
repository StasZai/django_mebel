from django.urls import path

from . import views

urlpatterns = [
    path("", views.MebelListView.as_view()),
    path("<slug:slug>/", views.MebelDetailView.as_view(), name="mebel_detail"),
]