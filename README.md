<h1>IF2250 - Public Recipe</h1>

<h2>Penjelasan singkat mengenai aplikasi</h2>
Perangkat yang lunak akan dirancang berbasis website dengan setidaknya 5 database, yaitu database pengguna, database shopper, database resep, database list pesanan yang ada, dan database alamat pengguna. Perangkat lunak dapat mengakses waktu pada time zone lokal secara terus menerus untuk memeriksa apakah dalam waktu pelayanan atau tidak. Perangkat lunak dapat beroperasi dengan efisiensi tinggi untuk kecepatan yang maksimal. Perangkat lunak memiliki User Interface yang dapat membuat user senang selama penggunaan. Untuk jangka panjang, perangkat lunak dapat dikembangkan dengan mudah.

<h2>Cara menjalankan aplikasi</h2>
<h3>Prasyarat:</h3>

- `pip install pandas`
- `pip install mysql-connector-python`
- `pip install csv`

<h3>Running Program</h3>

1. Jalankan `python main.py` di laptop anda
2. Selamat datang di public recipe, selamat berbelanja!


<h2>Daftar modul yang diimplementasi dilengkapi dengan nama modul, NIM dan nama penanggung jawab, dan capture screen tampilan layar (jika ada) permodul</h2>

Nama Modul | NIM/Nama penanggungjawab | Capture Screen 
--- | --- | ---
Registrasi dan Login | 13519191 - Kevin Ryan
Pembeli dan Total Harga | 13519169 - David Owen Adiwiguna | ![](img/logo.png)
Shopper dan Riwayat Pemesanan | 13519175 - Stefanus Jeremy Aslan |
Pencarian Resep dan Kontak Shoppercell | 13519215 - Leonard Matheus |

<h2>Daftar tabel basis data yang diimplementasi dilengkapi dengan nama tabel dan atributnya</h2>

Nama Tabel  | Atribut | Nama Tabel | Atribut
---------- | ------- | --- | ---
Pembeli.csv | <ul><li>nama_pembeli</li><li>no_telp_pembeli</li><li>email_pembeli</li><li>alamat</li><li>username</li><li>password</li></ul> | Pesanan.csv | <ul><li>Nama Pembeli</li><li>Alamat Pembeli</li><li>Telepon Pembeli</li><li>Nama Toko</li><li>Alamat Toko</li><li>Bahan</li></ul>
Shopper.csv | <ul><li>nama_shopper</li><li>no_telp_shopper</li><li>email_shopper</li><li>alamat_shopper</li><li>username</li><li>password</li></ul> | Riwayat.csv | <ul><li>ID</li><li>Tanggal</li><li>UserShopper</li><li>Pembeli</li><li>Alamat Pembeli</li><li>Telepon Pembeli</li><li>Nama Toko</li><li>Alamat Toko</li><li>Pesanan</li></ul>
