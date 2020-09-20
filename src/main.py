import shutil, os, re, sys, getopt
# TODO: receber os parâmetros como argumentos

# import sys, getopt

# def main(argv):
#    inputfile = ''
#    outputfile = ''
#    try:
#       opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
#    except getopt.GetoptError:
#       print 'test.py -i <inputfile> -o <outputfile>'
#       sys.exit(2)
#    for opt, arg in opts:
#       if opt == '-h':
#          print 'test.py -i <inputfile> -o <outputfile>'
#          sys.exit()
#       elif opt in ("-i", "--ifile"):
#          inputfile = arg
#       elif opt in ("-o", "--ofile"):
#          outputfile = arg
#    print 'Input file is "', inputfile
#    print 'Output file is "', outputfile

# if __name__ == "__main__":
#    main(sys.argv[1:])


PATH = './tests/tmp.txt'
TAGS = {
    'dbname': 'new_db',
    'container_name': 'thiscontainer'
}

def replace_tags(tags: dict, filepath: str):
    '''Troca cada tag pelo seu valor no arquivo em `filepath`'''
        # TODO: Find tags using regex
        
    # acha e altera as tags
    with open(f'{filepath}', 'r') as file:
        text = file.read()

    
    # reescreve o arquivo com as tags alteradas
    with open('tests/tmp.txt', 'w') as file:
        file.write(text)

def main():
    replace_tags(TAGS, PATH)

    # TODO: criar as pastas com a mesma arquitetura do exemplo_arq

    # TODO: rodar docker-compose com os.system()
    # ex: os.system("ls -la")



if __name__ =='__main__':
    main()