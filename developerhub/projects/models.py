from django.db import models
from users.models import Profile
from uuid import uuid4

class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) # null kwarg sets value to null in db, blank makes it not required for client input.
    featured_image = models.ImageField(null=True, blank=True, default='default.jpg')
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True) # Tag Class is referenced as a string, because it is defined below this one.
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['-createdAt']


class Review(models.Model):
    VOTE_TYPE = (
        ('UP', 'Up Vote'),
        ('down', 'Down Vote')
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.name