from django.shortcuts import render

from .models import Todo
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.http import HttpResponse

from TodoAPI.serializers import TodoSerializer

def index(request):
     return render(request, 'index.html')

class TodoList(generics.ListCreateAPIView):
  queryset = Todo.objects.all().order_by('-id')
  serializer_class = TodoSerializer

  def perform_create(self, serializer):
    serializer.save()


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Todo.objects.all()
  serializer_class = TodoSerializer

  # def get_queryset(self):
  #   return Todo.objects.all().filter(text=self.request.query_params)