from django.conf.urls import url, include
from django.contrib import admin
from issue_analysis import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('accounts.urls', namespace='accounts')),
#    url(r'^issues/', include('issues.urls', namespace='issues')),
]
