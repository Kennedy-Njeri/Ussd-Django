from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import africastalking


username = ""
api_key = ""
africastalking.initialize(username, api_key)
sms = africastalking.SMS


@csrf_exempt
def ussd_callback(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')

        response = ""

        sms_phone_number = []
        sms_phone_number.append(phone_number)

        # ussd logic
        if text == "":
            # main menu
            response = "CON What would you like to do?\n"
            response += "1. Check account details\n"
            response += "2. Check phone number\n"
            response += "3. Send me a cool message"
        elif text == "1":
            # sub menu 1
            response = "CON What would you like to check on your account?\n"
            response += "1. Account number"
            response += "2. Account balance"
        elif text == "2":
            # sub menu 1
            response = "END Your phone number is {}".format(phone_number)
        elif text == "3":
            try:
                # sending the sms
                sms_response = sms.send("Thank you for going through this tutorial", sms_phone_number)
                print(sms_response)
            except Exception as e:
                # show us what went wrong
                print(f"Houston, we have a problem: {e}")
        elif text == "1*1":
            # ussd menus are split using *
            account_number = "1243324376742"
            response = "END Your account number is {}".format(account_number)
        elif text == "1*2":
            account_balance = "100,000"
            response = "END Your account balance is USD {}".format(account_balance)
        else:
            response = "END Invalid input. Try again."

        return HttpResponse(response)
