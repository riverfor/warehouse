from django.contrib.admin.models import CHANGE, LogEntry
from users.models import User
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_text
from rest_framework import mixins, viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from django.db import transaction

from api.serializers.owner import OwnerSerializer, OwnerListSerializer


class ProfileView(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):

    serializer_class = OwnerSerializer
    queryset = User.objects.all()

    def list(self, request):
        with transaction.atomic():
            serializer_context = {
                'request': request,
            }
            queryset = self.queryset
            obj = get_object_or_404(queryset, pk=request.user.pk)
            serializer = OwnerListSerializer(obj, context=serializer_context)
            return Response(serializer.data)

    def retrieve(self, request, pk=None):
        with transaction.atomic():
            serializer_context = {
                'request': request,
            }
            queryset = self.queryset
            obj = get_object_or_404(queryset, pk=request.user.pk)
            serializer = OwnerListSerializer(obj, context=serializer_context)
            return Response(serializer.data)

    def update(self, request, pk=None):
        with transaction.atomic():
            serializer_context = {
                'request': request,
            }
            obj = User.objects.select_for_update().get(pk=request.user.pk)
            serializer = self.serializer_class(obj, context=serializer_context, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class CreateListView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin, viewsets.GenericViewSet):
    def get_object(self):
        with transaction.atomic():
            obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
            self.check_object_permissions(self.request, obj)
            return obj

    def perform_create(self, serializer):
        if serializer.save(owner=self.request.user):
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response({'status': 'fail', 'message': 'not set'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        """
        При обновлении объекта делаем запись в истории.
        """
        instance = self.get_object()
        response = super(CreateListView, self).update(
            request, *args, **kwargs
        )

        if response.status_code == 200:
            # insert into LogEntry
            # TODO: Change the message in order to include
            #       the fields that has been updated.
            message = [
                ('Изменено %(requestdata)s for %(name)s "%(object)s".') % {
                    'requestdata': force_text(request.data),
                    'name': force_text(instance._meta.verbose_name),
                    'object': force_text(instance)
                }
            ]
            LogEntry.objects.log_action(
                user_id=request.user.pk,
                content_type_id=ContentType.objects.get_for_model(
                    instance).pk,
                object_id=instance.pk,
                object_repr=force_text(instance),
                action_flag=CHANGE,
                change_message=message,
            )
        return response

