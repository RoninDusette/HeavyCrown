from django.conf.urls import url
from .views import HomeView, thanks

urlpatterns = [
    url(r'^$', HomeView.as_view()),
    url(r'thanks/', thanks, name='thanks'),
]