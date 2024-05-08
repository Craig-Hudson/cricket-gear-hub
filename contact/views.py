from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact_us(request):
    """
    Render the contact form page. If the form is submitted successfully,
    save the form data, send an email notification to the admin, and
    redirect to the contact success page.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Send email notification
            subject = 'New Contact Message'
            message = f'A new message has been received from {form.cleaned_data["name"]}.'
            sender = form.cleaned_data["email"]
            recipient = [settings.EMAIL_HOST_USER] 
            send_mail(subject, message, sender, recipient, fail_silently=False)
            return redirect('contact_success')  # Redirect to a success page
    else:
        form = ContactForm()
        
    return render(request, 'contact/contact.html', {'form': form})

def contact_success(request):
    """
    Render the contact success page after a successful form submission.
    """
    return render(request, 'contact/contact_success.html')
