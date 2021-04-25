from django.shortcuts import render

from src.mailings.mailchimp_services import add_mailchimp_email_with_tag


def webhook(request):
    """Обрабочик Вебхука от платежной системы"""
    add_mailchimp_email_with_tag(audience_name='DONATES',
                                 email=request.POST.get('email'),
                                 tag='DONATE')
