from django.urls import path
from .views import ArticleView, AuthorView

app_name = "articles"

# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('articles/<int:id>/', ArticleView.as_view(), name = "id"),
    path('authors/', AuthorView.as_view()),
]
