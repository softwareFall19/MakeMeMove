from django.shortcuts import redirect
from django.conf import settings
from django.core.mail import send_mail
from .models import Contact, ContactRental
from django.contrib import messages



def infoHome(request):
    if request.method == 'POST':
        #home = request.POST.get('home')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        home_id = request.POST.get('home_id')
        info = request.POST.get('info')
        user_id = request.POST.get('user_id')
        agent_email = request.POST.get('agent_email')

        contact_by_email = Contact(name=name, email=email, phone=phone, home_id=home_id, info=info, user_id=user_id)

        contact_by_email.save()

        send_mail(
            'Requesting Home Information',
            'A request for this home ' + home_id,
            settings.EMAIL_HOST_USER,
            [agent_email],
            fail_silently=False

        )
        send_mail(
            'Thank you for contacting MakeMeMove',
            'Thank you for contacting MakeMeMove, You will soon be contacted by an agent',
            settings.EMAIL_HOST_USER,
            [contact_by_email.email],
            fail_silently=False   
        )

        messages.success(request, "Thank you for your request, we will contact you shortly")
        return redirect('/homes/'+home_id)


def infoRental(request):
    if request.method == 'POST':
        #home = request.POST.get('home')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        rental_id = request.POST.get('rental_id')
        information = request.POST.get('information')
        user_id = request.POST.get('user_id')

        contact_by_email = ContactRental(name=name, email=email, phone=phone, rental_id=rental_id, information=information, user_id=user_id)

        contact_by_email.save()

        messages.success(request, "Thank you for your request, we will contact you shortly")
        return redirect('/renters/'+rental_id)

