import smtplib

gmail_user = 'julia4umak@gmail.com'
gmail_password = 'password'

sent_from = gmail_user
to = ['el.piankova@gmail.com']
subject = 'Lesson 4 Test email'
body = 'I did it!'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(gmail_user, gmail_password)

smtpObj.sendmail(sent_from, to, email_text)

smtpObj.close()

