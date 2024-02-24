# Penjelasan Kode main.py

1. Kode tersebut akan membuka video yang ditentukan dan menyimpannya ke dalam variabel `cap`

2. Kode tersebut akan mengambil range dari warna hijau dan merah dengan value yang memiliki format `BGR` yang selanjutnya akan dikonversi menjadi format `HSV`

3. Dengan menggunakan operasi Bitwise, kode akan mengaplikasikan range dari warna merah dan hijau sehingga hanya range pixel yang telah ditentukan oleh variable `mask` yang akan mucul di dalam frame