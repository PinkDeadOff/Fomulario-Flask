from flask import Flask ,request
from flask import render_template
from os import error
import smtplib

app = Flask(__name__)

subscribers = []

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USERNAME = 'yahir.carvajal99@gmail.com'
MAIL_DESTINATARIO = 'yahir.carvajal99@gmail.com'
MAIL_PASSWORD = 'zgkfbdxuhlgkvqwa'
MAIL_USE_TLS = True

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format


<b>Datos provenientes del WebSite.</b>
<h1 style = "purple" > Informacion del Usuario .</h1> 

<br>
|name| 

"""

@app.route('/form', methods=["POST"])
def form():
    first_name = request.form.get("first_name")
    body = request.form.get("body")
    email = request.form.get("email")

    if not first_name or not body or not email:
        error_statement = "All form fields requeried .."
        return render_template("main.html", error_statement = error_statement,
        first_name=first_name, body=body, email=email)    

    server = smtplib.SMTP(MAIL_SERVER, MAIL_PORT)
    server.starttls()
    server.login(MAIL_USERNAME, MAIL_PASSWORD)
    server.sendmail(MAIL_USERNAME, MAIL_DESTINATARIO, message.replace('|name|',str(body) + " - First Name: " + str(first_name) + " - Email: " +str(email) ) )
    server.quit()

    subscribers.append(f"{first_name} | {email}")
    return render_template("form.html", subscribers = subscribers)