import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd

def send_mass_mail(contacts, sender_email, sender_password, subject, message_template):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        
        for contact in contacts:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = contact['Email']
            msg['Subject'] = subject

            message = message_template.format(name=contact['Name'])
            msg.attach(MIMEText(message, 'plain'))

            server.sendmail(sender_email, contact['Email'], msg.as_string())
            print(f"Email sent to {contact['Name']} at {contact['Email']}")
        
        server.quit()
        print("All emails sent successfully!")
    except Exception as e:
        print("Failed to send emails:", e)

if __name__ == "__main__":
    contacts = pd.read_csv("contacts.csv").to_dict(orient='records')
    sender_email = "shibrajdeb456@gmail.com"
    sender_password = "ekzx tyys lsnp butq"
    subject = "Applying for Internship"
    message_template = "Dear HR,\n\nThis is your email message content.\n\nBest Regards,\nYour Name"

    send_mass_mail(contacts, sender_email, sender_password, subject, message_template)
