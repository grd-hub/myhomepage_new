from django.db import models


class InformationGerman(models.Model):
    guestbook_text = models.TextField()
    contact_text = models.TextField()


class InformationEnglish(models.Model):
    guestbook_text = models.TextField()
    contact_text = models.TextField()
