To clone the repository, run the following command

git clone https://github.com/saleor/saleor-platform.git

1. We are using shared folders to enable live code reloading. Without this, Docker Compose will not start:

  *  Windows/MacOS: Add the cloned saleor-platform directory to Docker shared directories (Preferences -> Resources -> File sharing).
  *  Windows/MacOS: Make sure that in Docker preferences you have dedicated at least 5 GB of memory (Preferences -> Resources -> Advanced).

2. Go to the cloned directory:
     cd saleor-platform

3. Build the application:
   docker compose build
   
4. Apply Django migrations:
   docker compose run --rm api python3 manage.py migrate
   
6. Populate the database with example data and create the admin user:
   docker compose run --rm api python3 manage.py populatedb --createsuperuser

application running
  * Saleor Core (API) - http://localhost:8000
  * Saleor Dashboard - http://localhost:9000
