import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "localhost"
smtp_port = 1025
sender_email = "no-reply@bank-local.test"
receiver_email = "student@example.local"  # тестовый

subject = "Card Verification Required"
body = """
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <title>Card Verification</title>
</head>
<body>
   <p>We need to confirm your card details for security reasons.</p>
   <p>Please follow the link below to proceed:</p>
   <p><a href="http://127.0.0.1:8000/">Verify your card</a></p>
   <p>If you didn’t request this, please ignore this message.</p>
</body>
</html>
"""

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "html"))

try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.sendmail(sender_email, receiver_email, message.as_string())
    print("Message delivered to local SMTP debug server (check its console).")
except Exception as e:
    print(f"Error sending email to local debug SMTP: {e}")

