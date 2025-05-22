from django.shortcuts import render

from .models import Topic

# Home page view: 
def index(request): 
    """Home page for blog."""
    return render(request, 'blog_app/index.html')

def topics(request): 
    """Show all topics."""
    
    # retrieve all topics: 
    topics = Topic.objects.order_by('date_added')
    
    # context is a dictionary of variables to pass to the template.
    # in this case, we pass one keys - topics and one value - a list of all topics.
    context= {'topics': topics}
    
    # 
    return render(request, 'blog_app/topics.html', context)

def topic(request, topic_id): 
    """Show a single topic."""

    # retrive the topic with the correcponding topic_id: 
    topic = Topic.objects.get(id=topic_id)
    
    # retrieve all entries associated with the topic and order in descending (minus sign) order by date: 
    entries = topic.entry_set.order_by('-date_added')

    # add the topic and the entries to the context: 
    context = {'topic': topic, 'entries': entries}
    
    return render(request, 'blog_app/topic.html', context)