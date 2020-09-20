cp ./src/docker-compose.yml ./tmp
cp ./src/Dockerfile ./tmp

python replace.py

cd tmp
sudo docker-compose up -d
