from django.core.mail import send_mail


def send(user_email):
    send_mail("test sending mail", 'Ny privet', 'd9285765@gmail.com', [user_email], fail_silently=False)

