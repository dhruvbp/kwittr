from django.conf.urls import patterns, url
from kwittr_messages import views


urlpatterns = patterns('',
    url(r'^$', views.message_listing, name='message_listing'),
    url(r'^(\d+)/$', views.message_details, name='message_details'),  
    url(r'^message_add_likes/(\d+)$', views.message_add_likes, 
        name='message.likes'),  
     
)

