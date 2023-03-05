import schedule

from client import Client, check_file, move_files


def handle_scheduled_tasks():
    client = Client('ftp.gnu.org', 'anonymous')
    client.list_files()
    print(check_file('files'))
    client.save_files('files')
    move_files('files', 'internal_network')
    client.disconnect()


if __name__ == '__main__':
    '''running the script every day at a given time'''
    schedule.every().day.at('14:58').do(handle_scheduled_tasks)
    while True:
        schedule.run_pending()
