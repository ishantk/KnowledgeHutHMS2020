import smtplib

message = "Hello All, This is hi from John"
sender = "john@example.com"
recipient = "fionna@example.com"

# Outgoing Mail Server for Google :)
mail = smtplib.SMTP("smtp.gmail.com", 587)

mail.starttls()

# Change Security in Google Account | Allow Less Secure Apps :)
mail.login(user=sender, password="pass123")
header = "To:"+recipient+"\n"+"From:"+sender+"\n"+"subject: this is a test mail\n"
content = header+message
mail.sendmail(sender, recipient, content)

mail.close()