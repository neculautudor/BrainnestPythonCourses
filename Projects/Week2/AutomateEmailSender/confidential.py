import os
'''set the api password from gmail from an outside file. Don't want to
share it here, as it's confidential. If you really need to run the project and you need it, contact me
(neculautudor02@gmail.com) or get the key to your own account and update both here'''
file = 'C:/Users/xtyan/Desktop/google_api_password.txt'
with open(file) as text:
    GOOGLEPASSWORD = text.readline()
SENDER = 's1ncegoku@gmail.com'
