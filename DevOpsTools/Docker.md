# Docker #

## Questions ##

can you rename a container after it is started?
how can you top multiple containers?

## Important Docker Commands ##

- List
  -  containers
     - `docker container ls`
   - networks
     - `docker network ls`
- Print Container Logs
  - `docker logs --tail 100 <containerid>`
- Run commands
  - Basic Run
    - `docker run --name <containername> <containerimage>`
  - Creates a pseudo-TTY connected to the containers stdin (-it)
    - `docker run -it ...`
  - Publish or expose port
    - `docker run -p 127.0.0.1:80/8080/tcp`
      - binds port 8080 of the container to TCP port 80 on local host
- Stop Commands
  - `docker stop <containername>`


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

## Resources ##

- [Docker Docs](https://docs.docker.com/engine/reference/commandline/run/) 
- [Docker Cheet Sheet](https://www.docker.com/sites/default/files/d8/2019-09/docker-cheat-sheet.pdf)
- [Setting up Docker on CentOs](https://docs.docker.com/engine/install/centos/)
- [Problems with Podman and Buildah](https://feitam.es/how-to-fix-error-problem-with-installed-package-podman-and-buildah-installed-docker-ce-in-centos/)
- [Postgres Docker Image](https://hub.docker.com/_/postgres)
- [Katacoda Docker Course](https://www.katacoda.com/courses/docker)
- [Docker Getting Started](https://docs.docker.com/get-started/overview/)
- [Packaging Docker Containers for Heroku](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml)
- [Play with Docker Training](https://training.play-with-docker.com/)
- [Containers are Not the Future](https://www.linkedin.com/pulse/containers-future-ian-eyberg/)
- [DISA Kubernetes Hardening Guide](https://media.defense.gov/2021/Aug/03/2002820425/-1/-1/1/CTR_KUBERNETES%20HARDENING%20GUIDANCE.PDF)
- [Docker Security Cheat Sheet](https://blog.gitguardian.com/how-to-improve-your-docker-containers-security-cheat-sheet/)