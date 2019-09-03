import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email you want to send the update from (only works with gmail)
fromEmail = 'justinferron@gmail.com'

# Email you want to send the update to
toEmail = 'justinferron@me.com'


def sendEmail(price, link, passwd):
    priceMessage = str(price)
    linkMessage = str(link)

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'GIER ALERT!!!'
    msgRoot['From'] = fromEmail
    msgRoot['To'] = toEmail
    msgRoot.preamble = 'GIER ALERT!!!'

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)
    msgText = MIMEText('de eshop kaarten zijn nu lager dan de prijs die je wilt!\r\n De prijs is : ' + priceMessage + '\r\n Link naar de website: ' + linkMessage)
    msgAlternative.attach(msgText)

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(fromEmail, passwd)
    smtp.sendmail(fromEmail, toEmail, msgRoot.as_string())
    smtp.quit()