# ledger
## Docker instruction

1. Start docker compose file

         sudo docker-compose up -d
2. Stop docker compose

         sudo docker-compose down
3. Check docker container
         
         sudo docker ps -a


## Installation instruction

1. Download Postgresql Docker or Install it manually.

        docker pull postgres:12.3
        docker run --name postgres-12.3 -e POSTGRES_PASSWORD=p -p 5432:5432 -d postgres:12.3
        
2. Create Database on Postgresql

        docker exec -it postgres-12.3 bash
        psql -U postgres
        CREATE DATABASE ledger WITH OWNER = postgres ENCODING = 'UTF8' LC_COLLATE = 'en_US.utf8' LC_CTYPE = 'en_US.utf8' TABLESPACE = pg_default CONNECTION LIMIT = -1;
