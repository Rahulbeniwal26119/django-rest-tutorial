from rest_framework.serializers import ModelSerializer
from pagination.models import Billing



class BillingSerializer(ModelSerializer):
    class Meta:
        model = Billing
        fields = '__all__'