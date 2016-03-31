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

# Proficiency Model
# defines one or more variables related to the knowledge,
# skills, and abilities we wish to measure.
class Competency(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    root = models.BooleanField(default=False)
    childrens = models.ManyToManyField('self')
    created_date = models.DateTimeField(auto_now_add=True)

class MatrizReferencia(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    created_date = models.DateTimeField(auto_now_add=True)
    competencies = models.ManyToManyField(Competency)

class Task(models.Model):
    DIFFICULTY = (
        ('E', 'Easy'),
        ('M', 'Medium'),
        ('H', 'Hard'),
    )
    title = models.CharField(max_length=200, verbose_name='Título')
    score = models.IntegerField;
    difficulty = models.CharField(max_length=1, choices=DIFFICULTY)
    user = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(auto_now_add=True)

class Evidence(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    created_date = models.DateTimeField(auto_now_add=True)
    tasks = models.ManyToManyField(Task)

