from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getContact(request):
   return Response()


"""REST API viewsets"""

from rest_framework import viewsets, response, decorators
from . import models, serializers


class UserViewSet(viewsets.ViewSet):
    """User sign up"""

    authentication_classes = []
    permission_classes = []
    serializer_class = serializers.UserModelSerializer

    def create(self, request):
        """Create new user action"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return response.Response(
            {"detail": f"user {user.username} created"}, status=201
        )


class ContactsViewSet(viewsets.ModelViewSet):
    """Contacts viewset"""

    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactModelSerializer

    @decorators.action(detail=False, methods=["post"])
    def auth(self, request):
        # Logica para autenticar al usuario
        email = request.data.get("email")
        password = request.data.get("password")
        return response.Response({"token": "lkajshdlkfjhaslkdjhflkasjhdfklj"})
