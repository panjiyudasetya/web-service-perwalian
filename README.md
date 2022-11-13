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

## API Design

### Mengambil Data Mahasiswa
```
GET http://localhost:8080/mahasiswa/

RESPONSE - 200
[
  {
    "id": 1,
    "nim": "11201",
    "nama_depan": "Panji",
    "nama_belakang": "Yudasetya Wiwaha",
    "alamat": "Batu Indah Regency, Bandung Barat",
    "tanggal_lahir": "2000-01-01",
    "angkatan": 2022
  },
  {
    "id": 2,
    "nim": "11202",
    "nama_depan": "Deni",
    "nama_belakang": "Ramdani",
    "alamat": "Bandung",
    "tanggal_lahir": "2000-02-02",
    "angkatan": 2022
  }
]
```
### Mengambil Data Dosen
```
GET http://localhost:8080/dosen/

RESPONSE - 200
[
  {
    "id": 1,
    "nid": "DS019-21",
    "nama_depan": "Chandra",
    "nama_belakang": "Poernama, M.Sc., Ph.D.",
    "alamat": "Bandung"
  },
  {
    "id": 2,
    "nid": "DS019-22",
    "nama_depan": "Jeffry",
    "nama_belakang": "Koesnaedi, M.Sc., Ph.D.",
    "alamat": "Bandung"
  }
]
```
### Mengambil Data Mata Kuliah
```
GET http://localhost:8080/mata-kuliah/

RESPONSE - 200
[
  {
    "id": 1,
    "kode": "WS_INTRO",
    "dosen": {
      "id": 1,
      "nid": "DS019-21",
      "nama_depan": "Chandra",
      "nama_belakang": "Poernama, M.Sc., Ph.D.",
      "alamat": "Bandung"
    },
    "nama": "Pengenalan Web Semantik",
    "sks": 3
  },
  {
    "id": 2,
    "kode": "BIG_DATA",
    "dosen": {
      "id": 2,
      "nid": "DS019-22",
      "nama_depan": "Jeffry",
      "nama_belakang": "Koesnaedi, M.Sc., Ph.D.",
      "alamat": "Bandung"
    },
    "nama": "Pengolahan Data Berskala Besar",
    "sks": 3
  }
]
```
### Mengambil Data Perwalian
```
GET http://localhost:8080/perwalian/

RESPONSE - 200
[
  {
    "id": 1,
    "kode": "PW01-20",
    "mahasiswa": {
      "id": 1,
      "nim": "11201",
      "nama_depan": "Panji",
      "nama_belakang": "Yudasetya Wiwaha",
      "alamat": "Batu Indah Regency, Bandung Barat",
      "tanggal_lahir": "2000-01-01",
      "angkatan": 2022
    },
    "dosen": {
      "id": 2,
      "nid": "DS019-22",
      "nama_depan": "Jeffry",
      "nama_belakang": "Koesnaedi, M.Sc., Ph.D.",
      "alamat": "Bandung"
    },
    "mulai_tahun_ajaran": 2022,
    "akhir_tahun_ajaran": 2023,
    "tanggal_perwalian": "2022-06-01",
    "masalah": "",
    "saran": ""
  }
]
```
### Mengambil Data Rencana Studi
```
GET http://localhost:8080/rencana-studi/

RESPONSE - 200
[
  {
    "id": 1,
    "kode_perwalian": "PW01-20",
    "mata_kuliah": {
      "id": 2,
      "kode": "BIG_DATA",
      "dosen": {
        "id": 2,
        "nid": "DS019-22",
        "nama_depan": "Jeffry",
        "nama_belakang": "Koesnaedi, M.Sc., Ph.D.",
        "alamat": "Bandung"
      },
      "nama": "Pengolahan Data Berskala Besar",
      "sks": 3
    },
    "grade": null
  },
  {
    "id": 2,
    "kode_perwalian": "PW01-20",
    "mata_kuliah": {
      "id": 1,
      "kode": "WS_INTRO",
      "dosen": {
        "id": 1,
        "nid": "DS019-21",
        "nama_depan": "Chandra",
        "nama_belakang": "Poernama, M.Sc., Ph.D.",
        "alamat": "Bandung"
      },
      "nama": "Pengenalan Web Semantik",
      "sks": 3
    },
    "grade": null
  }
]
```


