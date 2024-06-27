import smtplib

my_email = "sender email goes here"
my_password = "sender password goes here"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="receiving email goes here",
        msg= "Subject: Hello\n\nThis is the body of the email."
    )