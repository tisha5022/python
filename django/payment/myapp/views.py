from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import razorpay
from django.core.mail import send_mail
from django.conf import settings
import requests


# Create your views here.

def index(request):
    return render(request,"index.html")

def payment(request):
    amt = request.GET['amt']
    client = razorpay.Client(auth=("rzp_test_S1Hsg7YN8MlwDU", "ZKs1rK1XnjRDNd4uxjP2NcRJ"))

    
    data = { "amount": int(amt)*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) # Amount is in currency subunits.
    
    return JsonResponse(payment)


def sendmail(request):
    context = {}
  
    if request.method == 'POST':
        address = request.POST.get('address')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if address and subject and message:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                context['result'] = 'Email sent successfully'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
        else:
            context['result'] = 'All fields are required'
    
    return render(request,"mail.html",context)


def sendsms(request):
    

    url = "https://www.fast2sms.com/dev/bulkV2"

    querystring = {"authorization":"APIKEY","message":"This is test message","language":"english","route":"q","numbers":"8866280999"}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)