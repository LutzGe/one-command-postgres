FROM postgres:alpine


WORKDIR /app

COPY . /app

VOLUME [ "$host_dir:/app" ]

EXPOSE 80
USER $user

RUN PATH=$PATH:/
ENTRYPOINT [ "psql -c \"CREATE DATABASE $dbname\"; pg_restore -d $dbname $filename" ]




