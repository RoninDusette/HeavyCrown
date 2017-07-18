from django.views.generic import TemplateView
from HeavyCrown.apps.banner.models import BannerVideo


class HomeView(TemplateView):
    template_name = "djgui/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['banner_video'] = BannerVideo.objects.all()

        return context
