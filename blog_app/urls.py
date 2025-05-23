"""Define URL patterns for blog_app."""

from django.urls import path
from . import views
# dot means "from current direcory"

app_name = 'blog_app'
# this helps Django distinguish between several apps in the same project

urlpatterns = [
    # EXAMPLE: 
    # path('onboarding', views.onboardgin_view, name='onboarding'),
    # where urls is example.com/onboarding
    # call the onboarding_view function
    # and assign it the name 'onboarding'

    # Home page (empty string): 
    path('', views.index, name='index'),

    # page with all the topics: 
    path('topics/', views.topics, name='topics'),

    # page (pattern) for all topics: 
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # when a page with this pattern is requested, the `topic` (SINGULAR) view will be called 
    # and the integer between slashes will be passed to the view as the topic_id argument
]

