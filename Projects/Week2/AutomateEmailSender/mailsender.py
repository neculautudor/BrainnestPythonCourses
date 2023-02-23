import os
import smtplib
import ssl
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename

import logging
from confidential import GOOGLEPASSWORD, SENDER

'''only works with a gmail account as sender'''
GMAIL_PORT = 465

'''setting up the logger with logging anything over DEBUG level, and write the time as well as the message'''
logging.basicConfig(filename='logs.txt', level=logging.DEBUG, format="%(asctime)s %(message)s")



class MailSender():
    def __init__(self):
        '''using a secure protocol'''
        context = ssl.create_default_context()
        self.server = None
        try:
            '''i am using the gmail server to send the mail, and 465 is one of its ports'''
            self.server = smtplib.SMTP_SSL('smtp.gmail.com', GMAIL_PORT, context=context)
        except ValueError:
            logging.error(f'Could not connect to server because: \n {ValueError}')
            print(f'Could not connect to server because: \n {ValueError}')
        '''logging in to the gmail account first'''
        self.server.login(SENDER, GOOGLEPASSWORD)

    def send_mail(self, receivers: list[str], subject, message, files=None):
        '''composing and sending the actual mail'''

        '''validating the files'''
        validation = validate_files(files)
        if type(validation) == str:
            logging.error(validation)
            print(validation)
            return

        msg = MIMEMultipart()
        msg['From'] = SENDER
        msg['To'] = ' '.join(receivers)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))
        '''going through the files that need to be sent and adding them to the msg'''
        for f in files or []:
            try:
                '''rb for reading in binary'''
                fil = open(f, "rb")
                '''creating the MIMEApplication that will be attacked to the MIMEMultipart'''
                part = MIMEApplication(
                    fil.read(),
                    Name=basename(f)
                )
            except:
                logging.error('Could not open file')
                return
            '''after the file is closed, setting the type of content that is added and the name of the file that we send'''
            part['Content-Disposition'] = f'attachment; filename="{basename(f)}"'
            msg.attach(part)

        '''the SMTP.sendmail method receives a list of receivers as parameter, so i don't have to iterate through them myself'''
        self.server.sendmail(SENDER, receivers, msg.as_string())
        '''log all the emails sent'''
        logging.debug(f'Mail sent: Sender: {SENDER}, Receivers: {receivers}, Message: {msg.as_string()}')


def validate_files(files):
    '''
    :param files: the path to the files that is verified
    :return: String with the error or true if it's valid
    '''
    for file in files:
        if not os.access(file, os.F_OK):
            return f'ERROR! Path {file} cannot be accessed(probably does not exist)'
        if not os.access(file, os.R_OK):
            return f'ERROR! Cannot read file {file}'
    return True
