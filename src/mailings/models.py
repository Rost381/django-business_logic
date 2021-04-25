from django.db import models

class CommonMailingList(models.Model):
    """Рассылка на общие материалы дела"""
    email = models.EmailField('Email подписчика')

    class Meta:
        db_table = 'common_mailing_list'


class CaseMailingList(models.Model):
    """Рассылка на общие материалы Конкретного дела"""
    email = models.EmailField('Email подписчика')
    case = models.ForeignKey('cases.Case', on_delete=models.CASCADE, verbose_name='Дело')

    class Meta:
        db_table = 'case_mailing_list'
