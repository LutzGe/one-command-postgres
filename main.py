import shutil, os, re, sys, getopt

def get_args(argv):
    help_text = "Usage: main.py -d dbname -f filename [-u, --user][-c, --container]\nFor more options, try running config.py"
    
    if not argv:
        print(help_text)
        sys.exit()
    
    try:
        opts, args = getopt.getopt(argv,"f:d:uceh",["dbname=","filename=", "user=", "encoding="])
    except getopt.GetoptError:
        print(help_text)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(help_text)
            sys.exit()

        elif opt in ("-d", "--dbname"):
            TAGS['dbname'] = arg

        elif opt in ("-f", "--filename"):
            TAGS['filename'] = arg
        
        elif opt in ('-u', '--user'):
            TAGS['user'] = arg

        elif opt in ('-c', '--container'):
            TAGS['container_name'] = arg
        
        elif opt in ('-e', '--encoding'):
            TAGS['encoding'] = arg

def replace_tags(tags: dict, path: str):
    '''Troca cada tag pelo seu valor no arquivo em `filepath`'''
    
    for base_file in ('Dockerfile', 'docker-compose.yml'):
        with open(f'{path}/{base_file}', 'r') as file:
            text = file.read()

            # altera as tags
            for tag in tags.keys():
                text = text.replace('$'+tag, tags[tag])

        # reescreve o arquivo com as tags alteradas
        with open(f'{path}/{base_file}', 'w') as file:
            file.write(text)

def main():
    # Pega os argumentos passados no terminal
    get_args(sys.argv[1:])
    
    BASE_DIR = os.path.join(os.getcwd(), 'public/')
    HOST_DIR = os.path.join(os.getcwd(), f"{TAGS['dbname']}/")
    
    if TAGS['dbname'] in os.listdir():
        print('Pasta com o mesmo nome já existe')
        exit(1)
    
    TAGS['base_dir'] = BASE_DIR
    TAGS['host_dir'] = HOST_DIR

    # Cria a pasta com as cópias dos arquivos
    shutil.copytree(BASE_DIR, HOST_DIR)
    os.mkdir(os.path.join(HOST_DIR, 'volumes'))

    # Reescreve as tags
    replace_tags(TAGS, HOST_DIR)

    # Roda o container
    os.chdir(TAGS['host_dir'])
    os.system(f"docker-compose up -d")
    # os.system(f"docker exec -it {TAGS['container_name']} psql -d {TAGS['dbname']}")

TAGS = {
    'container_name': 'postgres_container',
    'dbname': 'new_db',
    'user': 'postgres',
    'password':'postgres',

    'pgadmin_email': 'email@email.com',
    'pgadmin_password': 'strongpassowrd',
}

if __name__ =='__main__':
    main()
    print(f"PG Admin email: {TAGS['pgadmin_email']}")
    print(f"PG Admin password: {TAGS['pgadmin_password']}")