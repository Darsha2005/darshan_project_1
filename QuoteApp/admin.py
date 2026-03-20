from django.contrib import admin
from .models import AuthorModel, QuoteModel

# Register your models here.

admin.site.register(AuthorModel)
admin.site.register(QuoteModel)