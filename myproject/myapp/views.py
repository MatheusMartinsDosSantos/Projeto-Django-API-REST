from rest_framework import generics
from myapp.models import Book
from myapp.serializers import BookSerializer
from django.views.generic.base import View
from django.http import JsonResponse

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDeleteView(View):
    def delete(self, request, *args, **kwargs):
        book = self.get_object()
        book.delete()
        return JsonResponse({'message': 'Livro deletado com sucesso.'})
    
    def get_object(self):
        pk = self.kwargs.get('pk')
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404