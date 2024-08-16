from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import send_mass_mail

# Create your views here.
def home(request):

 subject="Test_Mail from Django Server"
 message="This is a Demo-test mail"
 from_email="vivekverma9074@gmail.com"
 recipient_list=["vivek.satna100@gamil.com"]
 send_mail(subject,message,from_email,recipient_list,send_mail)

 return HttpResponse("please check your New_email")
