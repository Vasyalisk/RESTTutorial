#from django.http import Http404
from django.contrib.auth.models import User

#from rest_framework import status
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
#from rest_framework.views import APIView
#from rest_framework import mixins
from rest_framework import generics, permissions

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from snippets.permissions import IsOwnerOrReadOnly


#class SnippetList(APIView):
#    '''
#    List all snippets or create a new snippet.
#    '''
#    def get(self, request, format=None):
#        snippets = Snippet.objects.all()
#        serializer = SnippetSerializer(snippets, many=True)
#        return Response(serializer.data)
#
#    def post(self, request, format=None):
#        serializer = SnippetSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        else:
#            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

#class SnippetList(mixins.ListModelMixin,
#                  mixins.CreateModelMixin,
#                  generics.GenericAPIView):
#    '''
#    List all snippets or create a new snippet.
#    '''
#    queryset = Snippet.objects.all()
#    serializer_class = SnippetSerializer
#
#    def get(self, request, *a, **kw):
#        return self.list(request, *a, **kw)
#
#    def post(self, request, *a, **kw):
#        return self.create(request, *a, **kw)


class SnippetList(generics.ListCreateAPIView):
    '''
    List all snippets or create a new snippet.
    '''
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    

#class SnippetDetail(APIView):
#    '''
#    Retrieve, update or delete a snippet instance.
#    '''
#    def _get_object(self, pk): # made helper function private
#        try:
#            return Snippet.objects.get(pk=pk)
#        except Snippet.DoesNotExist:
#            raise Http404
#
#    def get(self, request, pk, format=None):
#        snippet = self._get_object(pk)
#        serializer = SnippetSerializer(snippet)
#        return Response(serializer.data)
#
#    def put(self, request, pk, format=None):
#        snippet = self._get_object(pk)
#        serializer = SnippetSerializer(snippet, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            # Do I need to return whole serializer data?
#            return Response(serializer.data)
#        else:
#            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#    def delete(self, request, pk, format=None):
#        snippet = self._get_object(pk)
#        snippet.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)
        

#class SnippetDetail(mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    generics.GenericAPIView):
#    '''
#    Retrieve, update or delete a snippet instance.
#    '''
#    queryset = Snippet.objects.all()
#    serializer_class = SnippetSerializer
#
#    # Specify *a an **kw?
#    def get(self, request, *a, **kw):
#        return self.retrieve(request, *a, **kw)
#
#    def put(self, request, *a, **kw):
#        return self.update(request, *a, **kw)
#
#    def delete(self, request, *a, **kw):
#        return self.destroy(request, *a, **kw)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieve, update or delete a snippet instance.
    '''
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
