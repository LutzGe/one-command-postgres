### Container com postgres em um comando(e alguns comandos)

### Comandos:

**Iniciando o script:**

#### 1. Coloque o seu arquivo .backup dentro da pasta public/
#### 2. Rode o seguinte comando dentro da pasta root do projeto:
`$ python3 main.py -f backup_file -d dbname`

**Acessando o PostgreSQL pelo terminal:**
<h5>` sudo `está sendo usando nesse contexto por que por padrão ele não vem com as permissões necessárias.</h5>
`$ sudo docker exec -it postgres_docker psql -d dbname`

---

## Acessando PgAdmin:
<h5>O container do PgAdmin está comentado por padrão em public/docker-compose.yml</h5>
<h5>Você deve descomentar aquele bloco e rodar o script novamente.</h5>

*<h6>Esses valores podem ser alterados dentro do arquivo docker-compose</h6>*

#### 1. Inspecione o container do PgAdmin e encontre o IPAddress e a porta
#### 2. Conecte-se no ip:porta para acessar a página de login do PgAdmin

*As credenciais serão mostradas no terminal ao término do script*
*[Work in progress] Podem ser alteradas rodando o script `config.py`*

## Créditos:

[@LutzGe](https://github.com/LutzGe)
---
