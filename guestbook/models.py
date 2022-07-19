from django.db import models
from django.core.validators import RegexValidator
from django.utils.text import slugify


class Guestbook(models.Model):
    author = models.CharField(max_length=30,
                              validators=[RegexValidator(r'[a-zA-Z][a-zA-Z][a-zA-Z]', message='wrong input')],
                              help_text='Please use at least 3 consecutive alphabetic characters')
    title = models.CharField(max_length=60,
                             validators=[RegexValidator(r'[a-zA-Z][a-zA-Z][a-zA-Z]', message='wrong input')],
                             help_text='Please use at least 3 consecutive alphabetic characters')
    text = models.TextField(max_length=3000)
    date_create = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = str(slugify(self.author)) + '_' + str(slugify(self.date_create))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
