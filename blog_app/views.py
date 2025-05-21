from django.shortcuts import render

# Create your views here.

# Home page view: 
def index(request): 
    """Home page for blog."""
    return render(request, 'blog_app/index.html')


