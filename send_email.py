import smtplib

class Send_Email():

    def __init__(self, subject, msg):
        self.subject = subject
        self.msg = msg

    def Send_Message(self):
        try:
            with smtplib.SMTP("smtp.gmail.com", port=587) as mail:
                email = "nerosamael7@gmail.com"
                password = "Samael666"
                mail.starttls()
                mail.login(user=email, password=password)
                mail.sendmail(from_addr=email, to_addrs=email, msg=f"Subject:{self.subject} \n\n{self.msg}")
                return 2
        except:
            return 1