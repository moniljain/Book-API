from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BookList,BookDetails

urlpatterns = {
					url(r'^books/$',BookList.as_view()),
					url(r'^books/(?P<pk>[0-9]+)/$',BookDetails.as_view()),
					url(r'^auth/',include('rest_framework.urls',namespace='rest_framework')),
				}

urlpatterns = format_suffix_patterns(urlpatterns)