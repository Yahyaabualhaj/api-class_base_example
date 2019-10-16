from rest_framework import routers, serializers, viewsets
from memberships.models import IdDocuments, Members
from django.contrib.auth.models import User


# Serializers define the API representation.
class IdDocumentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IdDocuments
        fields = ['id', 'id_type', 'id_no', 'f_name', 'expiry_date']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_active']


class MemberSerializer(serializers.ModelSerializer):
    # user = serializers.HyperlinkedRelatedField(
    #
    #     read_only=True,
    #     view_name='UserViewSet')
    #
    # id_document = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='id_document')

    class Meta:
        model = Members
        fields = ['user', 'id_document']
