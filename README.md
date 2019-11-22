# Ussd-Django

Create an Africastalking account
Navigate to Africastalking site and create an account. Login to your newly created account.

Create an app and you should see something like the image below.



Click on Go to Sandbox app. The next page is similar to the image below.


Click on Create channel This will take you to a page where you will create your own USSD service code. You will also be required to provide a callback url, but for the sake of this tutorial, we will make use of Ngrok. Ngrok is basically a software that provides a public url for accessing our local host. It listens from the same port that your local server is running on.


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