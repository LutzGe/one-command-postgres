import os

filename = 'tmp.txt'

if f'{filename}' in os.listdir('tests'):
    with open('tests/tmp.txt', 'r') as file:
        text = file.read()
        tags = {
            'apenas_tag':'LALALA', 
            'tag_mesma_linha':'MUITA COISA'
        }
        for tag in tags.keys():
            text = text.replace('$'+tag, tags[tag])
    
    with open('tests/tmp.txt', 'w') as file:
        file.write(text)

