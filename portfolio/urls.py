from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^enter-details/$', views.Portfolio_detail, name='Portfolio_detail'),
	url(r'^(?P<username>[\w.@+-]+)/(?P<pk>[0-9]+)/$', views.Portfolio_display, name='Portfolio_display'),
	url(r'^your-portfolios/$', views.View_all, name="View_all")
]