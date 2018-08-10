from django.conf.urls import url
from mlmodels import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^models/$', views.MLModelList.as_view()),
    url(r'^models/(?P<pk>[0-9]+)/$', views.MLModelDetail.as_view()),
    url(r'^params/$', views.ModelParamList.as_view()),
    url(r'^params/(?P<pk>[0-9]+)/$', views.ModelParamDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
