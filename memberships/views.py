from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication

from .models import IdDocuments, Members
from .serializers import IdDocumentsSerializer, UserSerializer, MemberSerializer
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import action


# ViewSets define the view behavior.
class IdDocumentsViewSet(viewsets.ModelViewSet):
    serializer_class = IdDocumentsSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = []

    def get_queryset(self):
        queryset = IdDocuments.objects.filter(id_type="Passport")
        return queryset


class UserViewSet(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication, ]
    queryset = User.objects.all()

    # def get_queryset(self):
    #     username = self.request.query_params.get('username', None)
    #     queryset = User.objects.all()
    #     if username is not None:
    #         queryset = User.objects.filter(username=username)
    #
    #     return queryset

    # serializer_class = UserSerializer

    # get all
    def list(self, request, *args, **kwargs):
        obj = User.objects.all()
        serializer = UserSerializer(obj, many=True)
        return Response(serializer.data)

    # get id=
    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = UserSerializer(obj)
        return Response(serializer.data)

    # post
    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # PUT
    def update(self, request, *args, **kwargs):
        user = self.get_object()

        user.username = 'Mr. ' + request.data['username']
        user.save()
        serializer = UserSerializer(user)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True)
    def deactivate(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = False
        user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data)

    @action(detail=True)
    def activate(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = True
        user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data)

    @action(detail=False)
    def deactivate_all(self, request, *args, **kwargs):
        user = User.objects.all()
        user.update(is_active=False)

        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def activate_all(self, request, *args, **kwargs):
        user = User.objects.all()
        user.update(is_active=True)

        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer
