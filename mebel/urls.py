from django.urls import path

from . import views

urlpatterns = [
    path("", views.MebelListView.as_view()),
    path("filter/", views.FilterMebelView.as_view(), name='filter'),
    path("<slug:slug>/", views.MebelDetailView.as_view(), name="mebel_detail"),
]