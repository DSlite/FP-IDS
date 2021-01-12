# FP-IDS: Limit bandwidth host yang melebihi kuota pada jaringan lokal dengan notifikasi Discord Webhook

* Nama: I Made Dindra Setyadharma
* NRP: 05311840000008

## EvilLimiter

Tool untuk melakukan limit terhadap jaringan lokal. Disini saya menambahkan beberapa potongan kode untuk menambah fungsionalitas agar dapat melakukan limitasi terhadap hosts pada jaringan lokal yang melebihi kuota penggunaan.

### Requirement

* Python 3+
* Linux Distribution

### Instalasi

clone ke direktori, lalu jalankan :

```bash
$ sudo python3 setup.py install
$ sudo evillimiter
```

Command lebih lanjut dapat dibaca pada CLI evillimiter

#### Command-Line Arguments

| Argument | Penjelasan |
| -------- | ----------- |
| ```-h``` | Menampilkan list command-line arguments |
| ```-i [Interface Name]``` | Menspesifikasikan interface jaringan (Didapatkan secara otomatis jika tidak dispesifikasikan)|
| ```-g [Gateway IP Address]``` | Menspesifikasikan alamat IP gateway (Didapatkan secara otomatis jika tidak dispesifikasikan)||
| ```-m [Gateway MAC Address]``` | Menspesifikasikan alamat MAC gateway (Didapatkan secara otomatis jika tidak dispesifikasikan)||
| ```-n [Netmask Address]``` | Menspesifikasikan netmask (Didapatkan secara otomatis jika tidak dispesifikasikan)||
| ```-f``` | Menghapus konfigurasi iptables dan tc pada jaringan|
| ```--colorless``` | Menonaktifkan pesan berwarna|

### Discord Webhook

Untuk mengirimkan notifikasi ke Discord, menggunakan discord-webhook sehingga lakukan langkah berikut

1. Dapatkan discord webhook URL untuk channel yang diinginkan
![image](https://user-images.githubusercontent.com/17781660/104198950-d0687680-5461-11eb-9549-9ec6ca18d435.png)
2. Masukkan discord webhook URL pada `evillimiter/console/io.py`
![image](https://user-images.githubusercontent.com/17781660/104199223-22110100-5462-11eb-9290-d09ef0788850.png)
3. Jalankan instalasi ulang dan notifikasi akan dikirimkan pada channel tersebut

### Contoh Penggunaan

1. Scanning
    ![image](https://user-images.githubusercontent.com/17781660/104325424-9bbcf380-5523-11eb-9a11-27812f0ff74c.png)
    ![image](https://user-images.githubusercontent.com/17781660/104325519-ad9e9680-5523-11eb-8b4f-4d16d216c9bc.png)
2. Limiting
    ![image](https://user-images.githubusercontent.com/17781660/104325653-d4f56380-5523-11eb-8e08-07fe01ac22a5.png)
    ![image](https://user-images.githubusercontent.com/17781660/104325679-dd4d9e80-5523-11eb-8068-4351472ff7ad.png)
3. Blocking
    ![image](https://user-images.githubusercontent.com/17781660/104326058-3ddcdb80-5524-11eb-869e-a0eb7437a794.png)
    ![image](https://user-images.githubusercontent.com/17781660/104326096-47664380-5524-11eb-8927-21abc800d3b7.png)
4. Auto
    ![image](https://user-images.githubusercontent.com/17781660/104326404-ac219e00-5524-11eb-89f4-e43631e37754.png)
    ![image](https://user-images.githubusercontent.com/17781660/104326494-c196c800-5524-11eb-9a80-6353959acfdd.png)
