from .models import Oilchange
from rest_framework import serializers

## Class OilchangeSerializer is a subclass of serializers.HyperlinkedModelSerializer.
## For serializing and deserializing data into representations such as json.
class OilchangeSerializer(serializers.HyperlinkedModelSerializer):
    ## Meta class is for configuring the OilchangeSerializer class.
    class Meta:
        # model to serialize
        model = Oilchange
        # fields to show in json
        fields = ('id', 'subject', 'details')