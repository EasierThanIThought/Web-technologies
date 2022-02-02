from django.db import models


class Feedback(models.Model):
    name = models.CharField('Никнейм', max_length=20)
    feedback = models.TextField('Отзыв')

    def __str__(self):
        return self.name
