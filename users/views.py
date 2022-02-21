
from rest_framework.response import Response
from django.contrib.auth.models import User
from . import models
from . import serializers
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import status
from rest_framework.decorators import action

class UsersViewSet(viewsets.ReadOnlyModelViewSet, mixins.UpdateModelMixin,\
                  mixins.CreateModelMixin,mixins.DestroyModelMixin):
    serializer_class = serializers.UsersSerializer
    queryset = models.Users.objects.all()


    @action(detail=True, methods=['GET','DELETE'])
    def relations(self,request, pk=None):
        print ("pk",pk)
        data_param = dict(request.query_params.items())
        if request.method == 'GET':
        
            if 'following_id' in data_param:
                queryset = models.Relations.objects.filter(follower_id=pk).filter(following_id=data_param['following_id'])
            else:
                queryset = models.Relations.objects.filter(follower_id=pk)
            return Response(queryset.values())

        elif request.method == 'DELETE':
            if 'following_id' in data_param:
                if models.Relations.objects.filter(follower_id=pk).\
                      filter(following_id=data_param['following_id']).exists():
                    models.Relations.objects.filter(follower_id=pk).\
                        filter(following_id=data_param['following_id']).delete()
                return Response('Relation removed')
            else:
                return Response('follower info not found',status=status.HTTP_404_NOT_FOUND)




class RelationsViewSet(viewsets.ReadOnlyModelViewSet, mixins.UpdateModelMixin, \
                       mixins.CreateModelMixin,mixins.DestroyModelMixin):
    serializer_class = serializers.RelationsSerializer
    queryset = models.Relations.objects.all()

