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
