
- Nama:Muhammad Firza Hermana putra
- NIM: 2509106090
- Kelas:B2'25 

Program ini merupakan program sederhana dengan tema Sistem Manajemen Toko Game dan digunakan untuk mengelola data game yang dijual, pelanggan, dan transaksi pembelian. Program ini merupakan pengembangan dari posttest sebelumnya dengan menambahkan konsep Relasi UML dan Inheritance.

Penjelasan Program: Program terdiri dari 7 class, yaitu:

class Game: digunakan sebagai superclass untuk semua jenis game. Menyimpan data game seperti ID, nama, harga, dan stok. Pada class ini terdapat atribut kelas untuk menyimpan nama toko, total game terdaftar, dan pajak PPN. Atribut harga dan stok dibuat protected agar bisa diakses oleh subclass. Terdapat instance method untuk menampilkan informasi game dan menambah stok, class method untuk membuat objek game dari dictionary, static method untuk mengecek validasi harga, serta property getter dan setter untuk mengakses atribut harga dan stok dengan validasi.

class GameFisik: merupakan subclass dari Game yang digunakan untuk menyimpan data game fisik atau kaset. Menggunakan super() untuk memanggil konstruktor superclass. Memiliki atribut unik yaitu kondisi (Baru/Bekas) dan platform (PS5, Nintendo, dll). Method tampilkan_info() di-override dari superclass untuk menampilkan informasi khusus game fisik. Terdapat method tambahan hitung_harga_final() yang memberikan diskon 30% untuk game bekas.

class GameDigital: merupakan subclass dari Game yang digunakan untuk menyimpan data game digital atau download. Menggunakan super() untuk memanggil konstruktor superclass. Memiliki atribut unik yaitu kode_download dan ukuran_file dalam GB. Method tampilkan_info() di-override dari superclass untuk menampilkan informasi khusus game digital. Terdapat method tambahan hitung_harga_final() yang menambahkan pajak digital 5%.

class Pelanggan: digunakan untuk menyimpan data pelanggan berupa ID, nama, dan saldo. Class ini memiliki atribut kelas untuk total pelanggan dan diskon member. Terdapat instance method untuk isi saldo, class method untuk mengubah diskon member global, static method untuk validasi saldo, serta property getter dan setter untuk mengakses atribut private saldo dengan validasi.

class Toko: digunakan untuk menyimpan data toko berupa nama dan alamat. Class ini menerapkan relasi agregasi dengan class Pelanggan, dimana toko menampung daftar pelanggan melalui method tambah_pelanggan(), namun pelanggan tetap bisa hidup mandiri tanpa toko.

class DetailTransaksi: digunakan untuk menyimpan detail item dalam transaksi berupa game, jumlah, dan subtotal. Class ini menerapkan relasi komposisi dengan class Transaksi, dimana objek DetailTransaksi dibuat di dalam Transaksi dan ikut musnah jika Transaksi dihapus.

class Transaksi: digunakan untuk menyimpan data transaksi berupa ID transaksi otomatis, tanggal, pelanggan yang membeli, game yang dibeli, dan jumlah pembelian. Class ini menerapkan relasi asosiasi dengan menerima objek Pelanggan dan Game sebagai parameter, serta relasi komposisi dengan membuat objek DetailTransaksi di dalamnya. Terdapat instance method untuk mencetak struk pembelian, class method untuk mendapatkan statistik transaksi, dan static method untuk menghitung total harga termasuk PPN.

Program menggunakan property setter untuk memvalidasi harga, stok, saldo, dan jumlah pembelian agar tidak menerima nilai yang kurang dari nol atau format yang tidak sesuai. Inheritance diterapkan pada class Game sebagai superclass yang diwarisi oleh GameFisik dan GameDigital, dimana kedua subclass menggunakan super().init() untuk memanggil konstruktor parent dan meng-override method tampilkan_info() dengan perilaku yang berbeda. Relasi UML diterapkan melalui asosiasi pada Transaksi yang menggunakan objek Pelanggan dan Game, agregasi pada Toko yang menampung daftar Pelanggan, dan komposisi pada Transaksi yang terdiri dari DetailTransaksi.
