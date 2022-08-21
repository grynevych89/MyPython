from django.shortcuts import render
from django.core.mail import send_mail
from .models import UserEmail, Feedback, Mailing


def index(request):
    return render(request, 'home/index.html')


def contact(request):
    if request.method == 'GET':
        return render(request, 'home/contact.html')
    elif request.method == 'POST':
        feedback = Feedback()
        feedback.subject = request.POST.get('subject')
        feedback.message = request.POST.get('message')
        feedback.user_email = request.POST.get('email')
        feedback.save()

        site_response = 'Ваше сообщение получено и будет обработано в течении дня'
        result = send_mail(feedback.subject, site_response, 'Grynevych',
                           [feedback.user_email], fail_silently=False)

        if result == 0:
            return render(request, 'home/failed.html')
        elif result == 1:
            return render(request, 'home/success.html')


def newsletter(request):
    if request.method == 'GET':
        return render(request, 'home/newsletter.html')
    elif request.method == 'POST':
        target_email = request.POST.get('email')
        message_body = """
            Уважаемый пользователь!
            Благодарим Вас за подписку на новостную рассылку.
            Я просто хотел еще раз поблагодарить Вас лично за то, что Вы интересуетесь новостями моего сайта. 
            Я очень ценю заинтересованных читателей, таких как Вы.

            Не стесняйтесь связаться со мной, если у Вас возникнут какие-либо вопросы.

            С уважением, Гриневич Николай
            Мой контактный номер: +38-095-215-91-75
            Telegram: @grynevych
        """
        user_email = UserEmail(email=target_email)
        user_email.save()
        try:
            result = send_mail('Подписка на Grynevych', message_body, 'Grynevych',
                               [target_email], fail_silently=False)
            if result > 0:
                return render(request, 'home/success.html')
            elif result == 0:
                return render(request, 'home/failed.html', context={
                    'reason': 'Сбой отправки почтового сообщения'
                })
        except RuntimeError:
            return render(request, 'home/failed.html', context={
                'reason': 'Сбой подключения к почтовому серверу'
            })
