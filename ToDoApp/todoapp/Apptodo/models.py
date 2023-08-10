from django.db import models

class FilmName(models.Model):
    title = models.CharField(("Film Adı"), max_length=50)

    def __str__(self):
        return self.title
