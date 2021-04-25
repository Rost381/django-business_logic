from django.db import models

class Case(models.Model):

    name = models.CharField('Название дела', max_length=255)

    class Meta:
        db_table = 'case'
