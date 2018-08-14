from rest_framework.viewsets import ModelViewSet
from mlmodels.models import MLModel, ModelParam
from mlmodels.serializers import MLModelSerializer, ModelParamSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response


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


class ModelParamBulkViewSet(ModelViewSet):
    queryset = ModelParam.objects.all()
    serializer_class = ModelParamSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.get("items") if 'items' in request.data else request.data
        many = isinstance(data, list)
        print (data, many)
        serializer = self.get_serializer(data=data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)