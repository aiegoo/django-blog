from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
from django.core.mail import BadHeaderError, EmailMessage
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseServerError, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import force_bytes

import requests
import hmac
from hashlib import sha1
from ipaddress import ip_address, ip_network

from django.views.decorators.http import require_POST

from .forms import ContactForm


def Home(request):
    if request.get_full_path() == "/kn/":
        return render(request, 'olora_frontend/index.kn.html')
    else:
        return render(request, 'olora_frontend/index.html')


@require_POST
def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid() and request.is_ajax():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']
            template = get_template('olora_frontend/contact_template.txt')
            context = {
                'name': name,
                'email': email,
                'message': message
            }
            content = template.render(context)
            try:
                email = EmailMessage(
                    subject,
                    content,
                    settings.SERVER_EMAIL,
                    ['tony.lightup.co.kr@gmail.com'],
                    headers={'Reply-To': email}
                )
                email.send()
                form.save()
            except BadHeaderError:
                return JsonResponse({"message": "error"})
        return JsonResponse({"message": "success"})


@require_POST
@csrf_exempt
def AutomateDeployment(request):
    # Verify if request came from GitHub
    forwarded_for = u'{}'.format(request.META.get('HTTP_X_FORWARDED_FOR'))
    client_ip_address = ip_address(forwarded_for)
    whitelist = requests.get('https://api.github.com/meta').json()['hooks']

    for valid_ip in whitelist:
        if client_ip_address in ip_network(valid_ip):
            break
    else:
        return HttpResponseForbidden('Permission denied.')

    # Verify the request signature
    header_signature = request.META.get('HTTP_X_HUB_SIGNATURE')
    if header_signature is None:
        return HttpResponseForbidden('Permission denied.')

    sha_name, signature = header_signature.split('=')
    if sha_name != 'sha1':
        return HttpResponseServerError('Operation not supported.', status=501)

    mac = hmac.new(force_bytes(settings.GITHUB_WEBHOOK_KEY), msg=force_bytes(request.body), digestmod=sha1)
    if not hmac.compare_digest(force_bytes(mac.hexdigest()), force_bytes(signature)):
        return HttpResponseForbidden('Permission denied.')

    # Process the GitHub events
    event = request.META.get('HTTP_X_GITHUB_EVENT', 'ping')

    if event == 'ping':
        return HttpResponse('pong')
    elif event == 'push':
        # Do something...
        return HttpResponse('success')
    return HttpResponse('pong')
