# API Template

Dockerized FastAPI application ready for dev and prd environments.

Includes _pytest_ testing framework.

## Development

Build: 

`docker-compose build`

Run:

`docker-compose up -d`


## Production

Build:

`docker build . -f docker/Dockerfile --no-cache -t api`

Run:

`docker run -d -p 8000:80 --name api api`
