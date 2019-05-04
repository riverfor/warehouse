from django.contrib.admin.models import LogEntry, CHANGE
from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from django.utils.encoding import force_text
from rest_framework import mixins, viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from base.viewsets import CreateListView
from api.serializers.incoming import ExpectedAcceptanceListSerializer, DocumentPlan, ExpectedAcceptanceSerializer, \
    AcceptanceProductsSerializer, DocumentProducts, AcceptanceProductsListSerializer, AcceptanceEntrySerializer
from incoming.models import DocumentEntry


class ExpectedAcceptanceListView(CreateListView):
    queryset = DocumentPlan.objects.all()

    def get_serializer_class(self):
        if self.action == 'update' or self.action == "create":
            return ExpectedAcceptanceSerializer
        else:
            return ExpectedAcceptanceListSerializer


class AcceptanceProductsView(CreateListView):
    queryset = DocumentProducts.objects.all()

    def get_serializer_class(self):
        if self.action == 'update' or self.action == 'create':
            return AcceptanceProductsSerializer
        else:
            return AcceptanceProductsListSerializer


class AcceptanceEntryView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin, viewsets.GenericViewSet):

    queryset = DocumentEntry.objects.all()
    serializer_class = AcceptanceEntrySerializer

    def get_object(self):
        with transaction.atomic():
            obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
            self.check_object_permissions(self.request, obj)
            return obj

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

    def perform_create(self, serializer):
        if serializer.save(owner=self.request.user):
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


