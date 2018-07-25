from .models import Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Book
		fields = ('id','name','genre','author','owner')