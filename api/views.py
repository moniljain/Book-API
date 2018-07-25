from django.shortcuts import render
from .serializers import BookSerializer
from rest_framework import generics
from .models import Book
# Create your views here.
class BookList(generics.ListCreateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	
	def perform_create(self,serializer):
		serializer.save(owner=self.request.user)
		
	
class BookDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
