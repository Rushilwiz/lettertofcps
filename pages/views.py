from django.shortcuts import render
from random import choice
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from config.settings import EMAIL_HOST_USER
from django.core.mail import EmailMultiAlternatives, send_mail

# Create your views here.

def main(request):
	if request.POST:
		subjects = [
			"Concerns with FCPS' proposal to change the TJ admissions system"
		]
		subject = choice(subjects)
		#recepient = request.POST.getlist('rep')
		recepient = ['rushilwiz@gmail.com', 'lettertofcps@gmail.com']
		context = {
			'form':request.POST,
			'mailto': f'mailto:{",".join(request.POST.getlist("rep"))}?subject={subject}',
			'maillist': ','.join(recepient),
			'subject': subject
		}
		html_message = render_to_string('pages/email_template.html', context=context)
		plain_message = strip_tags(html_message)
		sender = [request.POST.get('email')]
		email = EmailMultiAlternatives(
			subject, 
			plain_message, 
			EMAIL_HOST_USER, 
			recepient, 
			cc=sender,
			reply_to=sender
		)
		print(request.POST.getlist('rep'))
		email.attach_alternative(html_message, "text/html")
		print("### EMAIL SENT ###")
		print (recepient)
		email.send(fail_silently=False)
		return render (request, "pages/email.html", context=context)
	return render(request, "pages/index.html")
