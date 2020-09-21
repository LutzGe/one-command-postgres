FROM postgres:alpine


WORKDIR /app

COPY . /app

VOLUME [ "/home/lutz/dev/docker/postgres-docker-script/veiculos/:/app" ]

EXPOSE 80
USER postgres

# creating database[]
RUN [ "pwd" ]
ENTRYPOINT [ "psql -c \"CREATE DATABASE veiculos\"; pg_restore -d veiculos backup_veiculos.backup" ]




