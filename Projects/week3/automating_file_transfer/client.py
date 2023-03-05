import os, shutil, logging
from ftplib import FTP, error_perm

'''setting up the logger with logging anything over DEBUG level, and write the time as well as the message'''
logging.basicConfig(filename='logs.txt', level=logging.DEBUG, format="%(asctime)s %(message)s")


class Client:
    def __init__(self, server_name, user, password=None):
        '''Attempting to connect to the server, if there is no password we don't use one'''
        try:
            self.server = FTP(server_name)
            logging.debug(f'Connected to server {server_name}')
        except ValueError as msg:
            logging.error(f'Could not connect to server: {msg}')
        if password:
            self.server.login(user, password)
        else:
            self.server.login(user)

    def list_files(self):
        '''Using @data.append as the callback function for @server.dir, which will append the information about the files in
        @data line by line'''
        data = []
        self.server.dir(data.append)
        for line in data:
            print('-', line.split(' '))

    def get_files_names(self):
        '''@nlst is the method for getting the files names in the current directory'''
        return self.server.nlst()

    def files_names_generator(self):
        '''generator for returning the next file for each @next call'''
        files = self.get_files_names()
        for filename in files:
            yield filename

    def save_files(self, path):
        '''if path does not exist, a custom exception is raised'''
        if not check_file(path):
            logging.debug(f"File name or path '{path}' is incorrect")
            raise Exception("File name or path is incorrect")
        '''Creating the generator and iterating through it until it's done'''
        file_generator = self.files_names_generator()
        files_saved = 0
        while file_generator:
            filename = None
            try:
                '''try and except block used for avoiding raising an error when the generator has no next value'''
                try:
                    filename = next(file_generator)
                except StopIteration:
                    break
                self.server.retrbinary(cmd=f"RETR {filename}", callback=save_file(path, filename))
                files_saved += 1
                '''@server.retrbinary for retrieving each file and then saving it with the @save_file function as the callback'''\
            '''for the case that a file cannot be accessed, the user is notified and the process continues'''
            except error_perm as msg:
                logging.debug(f"Unable to retrieve file '{filename if filename else 'unknown'}' -  Error: {msg}")
                print(f"Unable to retrieve file '{filename if filename else 'unknown'}' -  Error: {msg}")
                continue
        logging.debug(f' {files_saved} Files saved')

    def disconnect(self):
        self.server.quit()
        logging.debug('Disconnected from the server')


def move_files(folder_from, folder_to):
    '''simply moving files from one folder to another, using @shutil.copy'''
    '''checking to see if source folder exists'''
    if not check_file(folder_from):
        logging.debug('Destination folder does not exist yet')
        return
    '''creating the destination folder if it does not exits'''
    if not check_file(folder_to):
        os.mkdir(folder_to)
    '''getting the files from the source folder'''
    files = os.listdir(folder_from)
    '''copying each file from the source folder to the destination folder'''
    for file in files:
        shutil.copy(f'{folder_from}/{file}', folder_to)
    logging.debug(f'Files moved from {folder_from} to {folder_to}')

def save_file(path, filename):
    '''returning a inner function for the purpose of being able to use @path and @filename as parameters on the callback function'''
    def inner(content):
        with open(os.path.join(path, filename), 'wb') as temp_file:
            temp_file.write(content)
            temp_file.close()
    return inner


def check_file(path):
    return os.path.exists(path)
