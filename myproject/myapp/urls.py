from django.urls import path
from myapp import views

urlpatterns = [
    path('books/', views.BookListCreateView.as_view()),
    path('books/<int:pk>/', views.BookRetrieveUpdateView.as_view()),
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view()),
]