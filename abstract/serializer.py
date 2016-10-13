from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

class ItemTypeField(serializers.Field):

    def to_representation(self, obj):
        return obj.model

    def to_internal_value(self, data):
        result = list(ContentType.objects.filter(model=data)[:1])
        if result:
            return result[0]
        raise serializers.ValidationError("No such content type %s" % data)


class GenericRelationsModelSerializer(serializers.ModelSerializer):
    item_type = ItemTypeField()

    def validate(self, data):
        objs = data['item_type'].model_class().objects \
            .filter(id=data['item_id'])
        if (not objs.count()):
            raise serializers.ValidationError("No such %s (id %d)"
                    % (data['item_type'].model, data['item_id']))
        return data
