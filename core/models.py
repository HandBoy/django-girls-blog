from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200, verbose_name='Título')
    text = models.TextField(verbose_name='Postagem', help_text='Informações')
    created_date = models.DateTimeField(
            auto_now_add=True)
    modified_date = models.DateTimeField(
            auto_now=True)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
