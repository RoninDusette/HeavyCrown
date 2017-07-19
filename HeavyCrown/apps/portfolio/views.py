from django.views.generic import DetailView
from .models import Photo


class PhotoDetail(DetailView):

    model = Photo
    template_name = "portfolio/photo-detail.html"
