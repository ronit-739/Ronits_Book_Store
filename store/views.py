from rest_framework.response  import Response
from rest_framework .decorators import api_view 
from rest_framework.exceptions import NotFound

from .models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def book_list(request):
    books=Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def book_create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['GET'])
def book_detail(request, id):
    try:
        book = Book.objects.get(id=id)  # Fetch a book by its 'id'
    except Book.DoesNotExist:
        raise NotFound("Book not found")  # Raise an error if the book is not found

    serializer = BookSerializer(book)  # Serialize the book
    return Response(serializer.data)

    