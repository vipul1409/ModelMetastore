from rest_framework import serializers

from mlmodels.models import MLModel, ModelParam


class ModelParamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelParam
        fields = ('key', 'value', 'model',)
        lookup_field = ('model', )


class MLModelSerializer(serializers.ModelSerializer):
    model_params = ModelParamSerializer(many=True, read_only=True)

    class Meta:
        model = MLModel
        fields = ('id', 'created_at', 'created_by', 'name', 'artifact_location', 'account_id',
                  'qbol_user_id', 'model_params')