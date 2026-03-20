from django.db import models

# Create your models here.

class AuthorModel(models.Model):
    authorName = models.CharField(max_length=200)
    authorDescription = models.TextField()

    def __str__(self):
        return self.authorName


class QuoteModel(models.Model):
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, related_name="quotes")
    quoteData = models.TextField()

    def __str__(self):
        return self.quoteData