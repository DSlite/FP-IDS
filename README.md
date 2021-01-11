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

### Discord Webhook

1. Dapatkan discord webhook URL untuk channel yang diinginkan
![image](https://user-images.githubusercontent.com/17781660/104198950-d0687680-5461-11eb-9549-9ec6ca18d435.png)
2. Masukkan discord webhook URL pada `evillimiter/console/io.py`
![image](https://user-images.githubusercontent.com/17781660/104199223-22110100-5462-11eb-9290-d09ef0788850.png)
3. Jalankan instalasi ulang dan notifikasi akan dikirimkan pada channel tersebut

### Contoh Penggunaan

1. Scanning