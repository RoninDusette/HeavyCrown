from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.conf import settings
from django.core.mail import send_mail
from HeavyCrown.apps.banner.models import BannerVideo
from HeavyCrown.apps.portfolio.models import Photo
from HeavyCrown.apps.quote.models import Quote
from .forms import ContactForm


class HomeView(FormView):
    template_name = "djgui/home.html"
    form_class = ContactForm
    success_url = "/thanks/"

    def form_valid(self, form):
        cd = form.cleaned_data
        send_mail(
            'You have a new message from' + cd['name'] + '-' + cd['sender'],
            cd['message'],
            cd['phone'],
            [settings.DEFAULT_TO_EMAIL],
            cd['address'],
            cd.get('email', settings.DEFAULT_FROM_EMAIL),
        )
        return HttpResponseRedirect('/thanks/')

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['banner_video'] = BannerVideo.objects.all()
        context['photos'] = Photo.objects.all()
        context['quotes'] = Quote.objects.all()

        return context


def thanks(request):
    return render(request, 'djgui/thanks.html')

