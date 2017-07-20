from django.conf.urls import url
from .views import PhotoDetail

urlpatterns = [
    url(r'(?P<pk>[-_\w]+)/$', PhotoDetail.as_view(), name='photo-detail'),
]