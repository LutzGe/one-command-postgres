# Arquivo para mudar algumas configurações do projeto
import dotenv



VARS.filename = input("Nome do arquivo (string incluindo a extensão, sem aspas):")
VARS.path     = input(f"Caminho relativo até o arquivo:")
VARS.dbname   = input(f"Nome da database:")

try:

    if (type(filename)  != type(str) or
       type(path)       != type(str) or
       type(dbname)     != type(str)):
        print("O nome do arquivo deve ser uma string.")
        exit

    dot = filename.index('.')
    filename = filename[:dot]
    ext = filename[dot + 1:]

except IndexError as e:

    print(e)
    print("Você deve incluir a extensão do arquivo")
    exit


###/  TODO #1: ADICIONAR TAGS NOVAS /###
# def ask_for_tags(flag_tags):
#     new_tags = dict()
#     while flag_tags:
#         key   = input('Tag:')
#         value = input('Valor:')

#         new_tags[key] = value

#         flag_tags = True if input('Outra? (y/n)') == 'y' else False
    
#     print(f"Novas tags: {new_tags.keys}")

#     VARS += new_tags

# new tags
print(f"Você adicionou novas tags nos arquivos 'docker-compose.yml' ou 'Dockerfile'?")
print(f"se sim, você poderá especificar elas em seguida.")

# TODO #1
# flag_tags = input()
# if flag_tags:
#     pass
# else:

###//###