from django.http import HttpResponse
from rest_framework import status
from django.http import Http404
from .models import Movie
from .serializer import MovieSerializer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt #csrf
from rest_framework.decorators import api_view

@csrf_exempt
@api_view(["GET", "POST"])
def movie_list(request, format=None):
    if request.method == "GET":
        
        if request.META['CONTENT_TYPE'] == "application/coffee-pot-command":
            detail = { "detail" : "The requested entity body is short and stout." }
            return Response(detail, status=418)

        serializer = MovieSerializer(Movie.objects.all(), many=True)

        if len(serializer.data) != 0:
            return Response(serializer.data)
        else:
            raise Http404
        
    elif request.method == "POST":
        try:
            if request.data["title"] == str(Movie.objects.get(title=request.data["title"])):
                detail = { "detail" : "title overlap."}
                return Response(detail, status=status.HTTP_409_CONFLICT)
        except Movie.DoesNotExist:
        
            
            serializer = MovieSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@csrf_exempt
@api_view(["GET", "PUT", "DELETE"])
def movie_detail(request, pk, format=None):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        raise Http404

    if request.method == "GET":
    
        if request.META['CONTENT_TYPE'] == "application/coffee-pot-command":
            detail = { "detail" : "The requested entity body is short and stout." }
            return Response(detail, status=418)
       

        serializer = MovieSerializer(movie)
        return Response(serializer.data)
        
    elif request.method == "PUT":
        if request.META['CONTENT_TYPE'] == "application/json":
            serializer = MovieSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        else:
            detail = { "detail" : "It only accepts application/json." }
            return Response(detail, status=status.HTTP_406_NOT_ACCEPTABLE)

    elif request.method == "DELETE":
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
