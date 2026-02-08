import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage

#sender = "pklakshmy442@gmail.com"
#receiver = "pklakshmi894@gmail@gmail.com"
#password = "ffdm umal bczz xixd"

#message = MIMEText("Sending email using Python")

#message["Subject"] = "Test Email"
#message["From"] = sender
#message["To"] = receiver

#server = smtplib.SMTP("smtp.gmail.com", 587)
#server.starttls()  # Encrypt the connection
#server.login(sender, password)
#server.quit()

#def send_email(sender,receiver,subject):
#    msg=MIMETEXT(anomaly detected in your system,user login and z_score>5,please find)
#  password="ffdm umal bczz xixd"
#   msg["Subject"]=subject
#    msg["From"]=sender
#    msg["To"]=receiver
#    with smtplib.SMTP("smtp.gmail.com",SMTP_PORT) as server:
#server.starttls()  
#        server.login(sender,password)
#        server.send_message(sender,reciever,message.as_string())
#server.quit()

#send email(
#"pklakshmy442@gmail.com",
#"pklakshmi894@gamil.com",
#"warning:anomaly detected",)

#when anomaly is detected and z-score >4 and less than -3
#prouter("/webhook/anomaly/detected/alert")
#def anomaly_detected():
#z-score
#if(z-score>4 && z-score<-3):
#    send_mail()
#z-score-[0.25,0.36,1.25,3.56,5.45]

EMAIL="pklakshmy442@gmail.com"
PASSWORD="ffdm umal bczz xixd"
SMTP_PORT=587




def send_mail(to_mail:str,anomaly:dict):
    subject="log anomaly detected"
body=f"""
anomaly detected in sysytem Logs
     time window:{anomaly["timestamp"]}
     error count:{anomaly["error_count"]}
     z_score:{anomaly["z_score"]}

     please review the log data
    
     Regards,
     lakshmy pk
      
    msg=EmailMessage()
    msg["Subject"]=subject
    msg["From"]=from_email
    msg["To"]=to_email
    msg.set_content(body)

    with smtplib.SMTP("smtp.gmail.com",SMTP_PORT) as server:
        server.starttls()
        server.login(pklakshmy442@gmail.com,ffdm umal bczz xixd")
        server.send_message(msg)"""

anomaly = {
    "timestamp": "2026-01-23 10:30",
    "error_count": 12,
    "z_score": 5.6
}

send_mail("pklakshmi894@gmail.com", anomaly)
