#!/usr/bin/env python3
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

log_file = "/Users/tayyisa/auca/InfoSec/Lab7/email_log.txt"
with open(log_file, "a") as f:
    f.write(f"Script run at {datetime.now()}\n")

smtp_server = "smtp.gmail.com"    
smtp_port = 587                    
sender_email = "rakhmatova_a@auca.kg" 
receiver_email = "asiyatrahmatova@gmail.com" 
password = "lqavllzbiltkraxe"      

msg = MIMEText(f"Hello!!!! Cron ran the script at {datetime.now()}")
msg["Subject"] = "Cron Test Email Lab7"
msg["From"] = sender_email
msg["To"] = receiver_email

try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
    with open(log_file, "a") as f:
        f.write(f"Email sent successfully at {datetime.now()}\n")
except Exception as e:
    with open(log_file, "a") as f:
        f.write(f"Error sending email at {datetime.now()}: {e}\n")

