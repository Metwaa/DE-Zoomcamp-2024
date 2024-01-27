# DE-Zoomcamp-2024
This repo created to do my Data Engineering ZoomCamp Projects as well as Module's Home Work.

# CodeSpace Step by step

After creating Repository in GitHub then create a New Codespace the do the below

# Check python
python --version

# check docker
docker --version

# instal list
pip install list

# install terraform 
wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list

sudo apt update && sudo apt install terraform

# install Jupyter nootebook
pip install jupyter


# Congrats! ;D
Codespace is ready for your amazing journey in Data Engineering ZoomCamp 2024.


# create docker network
docker network create pg-network

# create docker volume
docker volume create --name dtc_postgres_volume_local -d local

# run docker
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v dtc_postgres_volume_local:/var/lib/postgresql/data \
  -p 5432:5432 \
  --network=pg-network \
  --name pg-database \
  postgres:13

# run pgAdmin in a new terminal
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  --network=pg-network \
  --name pg-admin \
  dpage/pgadmin4

# Check container status if it's free or already allocated
docker ps -a

# To remove docker container 
docker rm -f [<docker id>]