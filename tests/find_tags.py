import os

VARS = {
    'filename': 'tmp.txt',
    'path': f'./',
    'dbname': 'new_db',
}

# def replaceTags(tag):

dirs = os.scandir('./')

def findTags():
    '''Procura as tags que são usadas no arquivo'''

    with open('tmp.txt', 'r+') as file:
        for line in file.readlines():
            amount = line.count('$')

            start_pos = 0
            for tag in range(amount):
                

                


# Info

# with open(f'{VARS.path}tmp.txt', 'r') as f:
#     tags = dict()
    
#     for line in f.readlines():
#         try:
#             pos = line.index('$')
        
#         except ValueError as e:
#             pass
        
#         else:
#             tag = line[pos:line[pos:].index(' ') + len(line[:pos])]


