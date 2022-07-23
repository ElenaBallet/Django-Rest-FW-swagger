from django.urls import path
from . import views

urlpatterns = [
    path('category', views.CategoryListAPIView.as_view(), name='categories'),
    path('authors', views.AuthorListAPIView.as_view(), name='authors'),
    path('ad', views.AdListAPIView.as_view(), name='ad'),
]