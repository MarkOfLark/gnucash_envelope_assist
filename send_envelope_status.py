import smtplib
import pickle
import datetime

from email_parameters import EmailParameters
from email.mime.text import MIMEText

def main():
    file = open('DO_NOT_COMMIT_email_parameters.dat','rb')
    param = pickle.loads(file.read())
    file.close()
    smtpserver = smtplib.SMTP(param.host,param.port)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(param.sender, param.passwd)


    msg = MIMEText('Fill me in!')
    msg['Subject'] = 'GnuCash Envelope Status:' + datetime.datetime.now().strftime('%Y-%m-%d')
    msg['From'] = param.sender
    msg['To'] =  ';'.join([str(x) for x in param.receivers]) 

    print(param)
    print(msg)
    smtpserver.sendmail(param.sender, param.receivers, msg.as_string())
    smtpserver.quit()


if __name__ == "__main__":
    # execute only if run as a script
    main()