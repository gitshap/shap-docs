from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.title