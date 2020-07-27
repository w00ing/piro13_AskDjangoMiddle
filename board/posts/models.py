from django.db import models


class Post(models.Model):

    """ Post Model Definition """

    title = models.CharField(max_length=25, verbose_name="Title")
    author = models.CharField(max_length=25, verbose_name="Author")
    content = models.TextField(verbose_name="Content")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
