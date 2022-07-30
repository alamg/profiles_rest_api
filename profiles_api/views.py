from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):
    """Test api view"""

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = ['Uses HTTP methods as functions(get, post, patch, put, delete)',
         'Is similar to a traditional Django view',
         'Gives you the most over you appllication logic',
         'Is mapped manualy to URLs']
        return Response({'message':'Hello', 'an_apiview':an_apiview})
