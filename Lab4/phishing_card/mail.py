import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "rakhmatova_a@auca.kg"  # Replace with your email address
sender_password = "uruf mlim orvo jsbw"     # Replace with your email password or app-specific password
receiver_email = "asiyatrahmatova@gmail.com"  # Replace with the recipient's email
subject = "Card Verification Required"
body = """
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <title>Card Verification</title>
</head>
<body>
   <p>We need to confirm your card details.</p>
   <p>Please follow the link below to proceed:</p>
   <p>file:///Users/tayyisa/auca/InfoSec/Lab4/phishing_card/index.html</p>
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
   server = smtplib.SMTP(smtp_server, smtp_port)
   server.starttls()
   server.login(sender_email, sender_password)
   server.sendmail(sender_email, receiver_email, message.as_string())
   print("Email sent successfully!")
except Exception as e:
   print(f"Error sending email: {e}")
finally:
   server.quit()
