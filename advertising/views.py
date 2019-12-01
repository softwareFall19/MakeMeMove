from django.conf import settings
from django.shortcuts import redirect, render
from django.core.mail import send_mail as email_admin
from django.contrib import messages

# from .models import Advertise
from .forms import AdvertiseForm



def advertising(request):
    if request.method == 'POST':
        form = AdvertiseForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data.get('role')
            name = form.cleaned_data.get('name')
            information = form.cleaned_data.get('information')
            telephone = form.cleaned_data.get('telephone')
            email = form.cleaned_data.get('email')
            form.save()

            # email subject, message
            subject = 'Contacting Admin for Advertise'
            ad_message = "{0}\n{1}\n{2}\n{3}\n{4}".format(
                role,
                name,
                information,
                telephone,
                email
            )
            from_email = settings.EMAIL_HOST_USER
            to_admin = [from_email, 'dfdavii@gmail.com']

            email_admin(
                subject,
                ad_message,
                from_email,
                to_admin,
                fail_silently=False,
            )
            messages.success(request, "Thank you for your request, we will contact you shortly")
            return redirect('index')
    else:
        form = AdvertiseForm()

    context = {
        'form': form
    }

    return render(request, 'advertising/advertising.html', context)