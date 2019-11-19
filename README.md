# Ussd-Django


Install and Use Ngrok
Download ngrok zip file, unzip the file and move it to /usr/local/bin PATH.

Run ngrok in the terminal using the following command.

ngrok http 8000
The default port for Django is 8000, which is what we have used.

Running ngrok takes you to a page where you can copy the generated public url. This url changes every time we run run ngrok.

Starting and Setting up the USSD App
Go to our Django project and locate the settings.py file. Paste the url inside the square brackets

ALLOWED_HOSTS = [ ]
Run the Django server using the following command after you must have activated the virtual environment where the africastalking_demo project is located.

python manage.py runserver
Also Go ahead to Africastalking, the Create a channel page and fill in your ngrok public url.

Click on Launch simulator to test your new USSD app.