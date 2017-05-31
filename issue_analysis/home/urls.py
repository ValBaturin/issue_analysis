from django.conf.urls import url
from home.views import HomeView, AllView, OwnView
from . import views

urlpatterns = [
    url(r'^add$', HomeView.as_view(), name='add'),
    url(r'^all$', AllView.as_view(), name='all'),
    url(r'^my', OwnView.as_view(), name='own'),
]
