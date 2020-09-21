import os

filename = 'tmp.txt'

if f'{filename}' in os.listdir('tests'):
    with open('tests/tmp.txt', 'r') as file:
        text = file.read()
        tags = {
            'container_name': 'postgres_container',
            'dbname': 'new_db',
            'user': 'postgres',
            'password': 'postgres',

            'pgadmin_email': 'email@email.com',
            'pgadmin_password': '5tr0ngp4ssw0rd',
        }
        for tag in tags.keys():
            text = text.replace('$'+tag, tags[tag])
    
    with open('tests/tmp.txt', 'w') as file:
        file.write(text)

