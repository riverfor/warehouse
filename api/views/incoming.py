from base.viewsets import CreateListView
from api.serializers.incoming import ExpectedAcceptanceListSerializer, DocumentPlan, ExpectedAcceptanceSerializer


class ExpectedAcceptanceListView(CreateListView):
    queryset = DocumentPlan.objects.all()

    def get_serializer_class(self):
        if self.action == 'update' or self.action == "create":
            return ExpectedAcceptanceSerializer
        else:
            return ExpectedAcceptanceListSerializer
