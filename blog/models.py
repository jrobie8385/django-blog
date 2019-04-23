from django.db import models

# Create your models here.
#  What to include in a blog application:
#    title, author, body


"""
we’re importing the class models and then creating a subclass of models.Model
called Post. Using this subclass functionality we automatically have access to everything
within django.db.models.Models and can add additional fields and methods as
desired.
"""

class Post(models.Model):
    title = models.CharField(max_length = 64)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE) #allowing for a many-to-one relationship
        # a given user can be the author of many different blog posts but not the other way around.
        #  For all many-to-one relationships such as a ForeignKey we must also specify an on_delete option.
    text = models.TextField()


     #link to fields available: https://docs.djangoproject.com/en/2.1/topics/db/models/#fields

    def __str__(self):
        return self.title

    #def get_absolute_url(self):
    #    return reverse("blog:detail", kwargs = {"authorName": self.author.username, "pk":self.pk})
