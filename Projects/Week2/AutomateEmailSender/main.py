''' You work at a company that sends daily reports to clients via email. The goal of this project is to automate the process of sending these reports via email.

Here are the steps you can take to automate this process:

    Use the smtplib library to connect to the email server and send the emails.

    Use the email library to compose the email, including the recipient's email address, the subject, and the body of the email.

    Use the os library to access the report files that need to be sent.

    Use a for loop to iterate through the list of recipients and send the email and attachment.

    Use the schedule library to schedule the script to run daily at a specific time.

    You can also set up a log file to keep track of the emails that have been sent and any errors that may have occurred during the email sending process. '''
from mailsender import MailSender
import schedule
'''In order to successfully run this project, you will need to set your own gmail account in the confidential.py file, and 
also generate a key for it from google accounts, and set that as well'''
if __name__ == '__main__':
    mailsender = MailSender()
    schedule.every().day.at('21:00').do(lambda:
        mailsender.send_mail(
            receivers = ['neculautudor02@gmail.com', 'tudortest@mailinator.com', ],
            subject = 'subject example',
            message = 'text example',
            files = ['C:/Users/xtyan/Desktop/attachment_example.txt']
        )
    )
    while True:
        schedule.run_pending()
