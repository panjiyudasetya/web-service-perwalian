# Web Service Sederhana untuk Perwalian

Proyek Web Service ini berbasis REST API menggunakan JSON sebagai response API-nya.

Entitas Relasional Diagram terkait project ini dapat dilihat pada gambar berikut ini:

![image](https://user-images.githubusercontent.com/21379421/201514531-dac78d7e-5f5b-417e-89c9-42f997849417.png)

Adapun batasan masalah pada project ini adalah sebagai berikut:
- Projek ini anya digunakan sebagai tugas studi, dan tidak memiliki persyaratan untuk menerapkan sistem autentikasi.
- Dapat yang tersedia diakses oleh publik.
- Web Service terbatas hanya untuk menangani `GET` request.

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
