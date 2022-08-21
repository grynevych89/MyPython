from django.shortcuts import render
from django.core.mail import send_mail
from .models import UserEmail, Feedback, Mailing


def index(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')


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
        result = send_mail(feedback.subject, site_response, 'MySite',
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
            Hello, dear User!
            
            You have subscribed to the newsletter
            from MySite
            We are open 24/7!
            
            We will be glad to be of service to you!
            Come back more often!
        """
        user_email = UserEmail(email=target_email)
        user_email.save()
        try:
            result = send_mail('Subscribe', message_body, 'MySite',
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


def success(request):
    return render(request, 'home/success.html')


def failed(request):
    return render(request, 'home/failed.html')


def admin_page(request):
    emails = UserEmail.objects.all()
    if request.method == 'GET':
        return render(request, 'home/admin_page.html', context={
            'emails': emails
        })
    elif request.method == 'POST':
        mailing = Mailing()
        mailing.subject = request.POST.get('subject')
        mailing.message = request.POST.get('message')
        mailing.author = request.POST.get('author')
        mailing.save()

        email_list = []
        for e in emails:
            email_list.append(e.email)

        html = """
            <h2>Сообщение в формате HTML</h2>
            <hr />
            <h3 style="color: purple">Информация о скидках...</h3>
        """

        result = send_mail(mailing.subject, mailing.message, f'MySite - {mailing.author}',
                           email_list, fail_silently=False, html_message=html)

        if result == 0:
            return render(request, 'home/failed.html', context={
                'reason': 'Сбой отправки почтовых сообщений'
            })
        else:
            return render(request, 'home/success.html')


def video_page(request):
    video1 = 'video1.mp4'
    return render(request, 'home/video_page.html', context={
        'video_file_name': video1
    })
