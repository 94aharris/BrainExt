# Docker #

## Setting Up Docker-ce on Centos ##

- Remove any old version
- Setup the Docker Repository
  
  ```bash
 sudo yum install -y yum-utils

 sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
```

- Install Docker

```bash
sudo yum install docker-ce docker-ce-cli containerd.io
```

  - Note if you receive conflict errors then you need to uninstall podman and buildah

```bash
sudo yum -y remove podman buildah
```

- Start Docker and verify it is running correctly with the hello-world image

```bash
sudo systemctl start docker
sudo docker run hello-world
```

- You need to use Sudo to use Docker (docker runs client server)

## Run a Docker PostgreSQL image ##

- Install Docker as outlined above
- Start a postgres instance with mapping to 5432
  `docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 postgres`
- default postgres user and db are created in the entrypoint with initdb
- Connect to psql (if you have psql clients installed)
  - 

## Important Docker Commands ##

- List containers
  - `docker container ls`
- Print Container Logs

## Resources ##

- [Docker Cheet Sheet](https://www.docker.com/sites/default/files/d8/2019-09/docker-cheat-sheet.pdf)
- [Setting up Docker on CentOs](https://docs.docker.com/engine/install/centos/)
- [Problems with Podman and Buildah](https://feitam.es/how-to-fix-error-problem-with-installed-package-podman-and-buildah-installed-docker-ce-in-centos/)
- [Postgres Docker Image](https://hub.docker.com/_/postgres)
- [Katacoda Docker Course](https://www.katacoda.com/courses/docker)
- [Docker Getting Started](https://docs.docker.com/get-started/overview/)
- [Packaging Docker Containers for Heroku](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml)
- [Play with Docker Training](https://training.play-with-docker.com/)
- [Containers are Not the Future](https://www.linkedin.com/pulse/containers-future-ian-eyberg/)