import pickle
    
class EmailParameters:
   def __init__(self, sender, receviers, passwd, host, port):
       self.sender = sender
       self.receivers = receviers
       self.passwd = passwd
       self.host = host
       self.port = port

def main():
    sender = input("What email address should be used for sending? ")
    receivers = input("What email address(es) should receive? (use a , to separate) ").split(",")
    passwd = input("What is the sending address passwd? (WARNING: not stored securely!) ")
    host = input("What is the host name of the SMTP server? ")
    port = int(input("What is the port number of the SMTP service? "))

    parm = EmailParameters(sender,receivers,passwd,host,port)
    parm_json = pickle.dumps(parm);

    file = open('DO_NOT_COMMIT_email_parameters.dat','wb');
    file.write(parm_json);
    file.close()


if __name__ == "__main__":
    # execute only if run as a script
    main()