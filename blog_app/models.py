from django.db import models

class Topic(models.Model):
    """A topic the user is posting about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__ (self): 
        """Return a string representation of the model.""" 
        return self.text

class Entry (models.Model): 
    """Subject of a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta: 
        verbose_name_plural = 'entries'
        # Meta.verbose_name_plural specifies the plural name for the model in the admin interface.
    
    def __str__ (self): 
        """Return a string representation of the model.""" 
        str_rep = f"{self.text[:50]}..." if len(self.text) > 50 else f"{self.text}"
        return f"{str_rep}"

