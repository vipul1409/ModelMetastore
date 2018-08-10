from mlmodels.models import MLModel, ModelParam
from mlmodels.serializers import MLModelSerializer, ModelParamSerializer
from rest_framework import generics


class MLModelList(generics.ListCreateAPIView):
    queryset = MLModel.objects.all()
    serializer_class = MLModelSerializer


class MLModelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MLModel.objects.all()
    serializer_class = MLModelSerializer


class ModelParamList(generics.ListCreateAPIView):
    queryset = ModelParam.objects.all()
    serializer_class = ModelParamSerializer


class ModelParamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ModelParam.objects.all()
    serializer_class = ModelParamSerializer
