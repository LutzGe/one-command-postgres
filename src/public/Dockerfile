FROM postgres:alpine


WORKDIR /app

COPY . /app

VOLUME [ "/var/run/postgresql:/var/run/postgresql" ]

EXPOSE 80
USER postgres

# creating database
RUN createdb -T $ newdb
RUN pg_restore -d newdb db.dump

# Inserting the specified db 
#RUN psql -d blioteca_dados < copia_bd_biblioteca.sql



