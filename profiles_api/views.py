from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from profiles_api import permission
from profiles_api import serializers
from profiles_api import models

class HelloAPIView(APIView):
    """Test api view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = ['Uses HTTP methods as functions(get, post, patch, put, delete)',
         'Is similar to a traditional Django view',
         'Gives you the most over you appllication logic',
         'Is mapped manualy to URLs']
        return Response({'message':'Hello', 'an_apiview':an_apiview})

    def post(self, request):
        """ Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response ({'message': message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handle partial updating an object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSets"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ Return a hello massage"""
        a_viewset = ['Uses actions(list, create, retrive, update, partial_update)',
        'Automatically maps to urls using Routers',
        'Provide more functinality with less code',

        ]
        return Response({'message':'Hello', 'a_viewset':a_viewset})

    def create(self, request):
        """Create a hello message with our name"""
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrive(self, request, pk=None):
        """ Handale getting an object by its ID"""
        return Response({'HTTP METHOD':'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'HTTP METHOD': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'HTTP METHOD': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'HTTP METHOD', 'DELETE'})


class userProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permission.UpdateOwnprofie,)
