import smtplib
from email.mime.text import MIMEText

sender_email = "your_email@gmail.com"
receiver_email = "receiver_email@gmail.com"
password = "your_password"

message = MIMEText("This email send by python")
message["Subject"] = "Python automaiton"
message["From"] = sender_email
message["To"] = receiver_email

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
