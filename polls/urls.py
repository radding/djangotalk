from django.conf.urls import include, url
from django.contrib import admin
from polls.views import index, voteUpAns, viewAllPolls, viewPoll, viewPoll2

urlpatterns = [
    # Examples:
    # url(r'^$', 'djangotalk.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^view/all/', viewAllPolls),
    url(r'^view/(?P<pollID>\d+)/$', viewPoll),
    url(r'^view/2/(?P<pollID>\d+)/$', viewPoll2),
    url(r'^vote/(?P<ansID>\d+)/$', voteUpAns, name = "vote"),
    url(r'$', index),
]

