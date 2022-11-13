# Web Service Sederhana untuk Perwalian

Proyek Web Service ini berbasis REST API menggunakan JSON sebagai response API-nya.

## Prerequisite

### Docker

Web Service ini dijalankan menggunakan _Docker containers_. Bagaimana kontainer dijalankan, semuanya diatur dengan menggunakan _docker-compose_. Untuk menginstall Docker pada komputer, Anda dapat mengikuti tautan dibawah ini:

Untuk mesin komputer dengan sistem operasi **MacOS**, cara instalasi Docker dapat ditemukan [disini](https://docs.docker.com/docker-for-mac/install/)

Untuk mesin komputer dengan sistem operasi **Linux**, cara instalasi Docker dapat ditemukan [disini](https://docs.docker.com/desktop/install/linux-install/)

Pastikan juga _command_ _`docker-compose`_ terinstall dengan benar agar Anda dapat menjalankan projeknya tanpa ada masalah.

### How to Start the Project

```
$ docker-compose up --build
```

### How to stop the Project

```
$ docker-compose down --remove-orphans
```
