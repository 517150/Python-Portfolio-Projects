from cryptography.fernet import Fernet

'''
def generate_key():
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)
'''


def load_key():
    return open('secret.key', 'rb').read()


key = load_key()
fer = Fernet(key)


def create():
    name = input('Account Name: ')
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as f:
        encrypted_pwd = fer.encrypt(pwd.encode())
        f.write(f'{name} | {encrypted_pwd.decode()} \n')


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip()
            user, encrypted_pwd = data.split('|')
            decrypted_pwd = fer.decrypt(encrypted_pwd.encode()).decode()
            print(f'User: {user} | Password: {decrypted_pwd}')


while True:
    mode = input('CREATE or VIEW password (or Q to QUIT): ').lower()
    if mode == 'q':
        break
    elif mode == 'create':
        create()
    elif mode == 'view':
        view()
    else:
        print('Invalid mode.')
        continue
