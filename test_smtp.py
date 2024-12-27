import smtplib

def test_smtp_connection(smtp_server, smtp_port, email, password):
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email, password)
        print("SMTP connection successful!")
        server.quit()
    except Exception as e:
        print("Failed to connect to SMTP server:", e)

if __name__ == "__main__":
    smtp_server = "smtp.gmail.com"
    smtp_port = 465
    email = "shibrajdeb456@.com"
    password = "ekzx tyys lsnp butq"  

    test_smtp_connection(smtp_server, smtp_port, email, password)
