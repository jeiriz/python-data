import smtplib
from getTemplate import getTemplate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp = smtplib.SMTP(host='smtp.gmail.com', port=587)
smtp.starttls()
smtp.login('juan.eiriz@alu.ifts18.edu.ar','ifts1324Utnfacultad')

mail = getTemplate('scraping/template.txt')

msg = MIMEMultipart() #create message

        # setup the parameters of the message
msg['From']='juan.eiriz@alu.ifts18.edu.ar'
msg['To']='juan.eiriz@alu.ifts18.edu.ar'
msg['Subject']="This is TEST"

msg.attach(MIMEText('plain'))
smtp.send_message(msg)
del msg

