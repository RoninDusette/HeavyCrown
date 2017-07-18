from django.views.generic import TemplateView
from HeavyCrown.apps.banner.models import BannerVideo
from HeavyCrown.apps.portfolio.models import Photo
from HeavyCrown.apps.quote.models import Quote


class HomeView(TemplateView):
    template_name = "djgui/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['banner_video'] = BannerVideo.objects.all()
        context['photos'] = Photo.objects.all()
        context['quotes'] = Quote.objects.all()

        return context
