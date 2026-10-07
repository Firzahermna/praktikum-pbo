------------Sistem Manajemen Toko Game--------------

Program ini merupakan program sederhana dengan tema Sistem Manajemen Toko Game dan digunakan untuk mengelola data game yang dijual, pelanggan, dan transaksi pembelian.

Penjelasan Program: Program terdiri dari 3 class utama, yaitu:

class Game: digunakan untuk menyimpan data game seperti ID, nama, harga, dan stok. Pada class ini terdapat atribut kelas untuk menyimpan nama toko, total game terdaftar, dan pajak PPN. Terdapat instance method untuk menampilkan informasi game dan menambah stok, class method untuk membuat objek game dari dictionary, static method untuk mengecek validasi harga, serta property getter dan setter untuk mengakses atribut private harga dan stok dengan validasi.

class Pelanggan: digunakan untuk menyimpan data pelanggan berupa ID, nama, dan saldo. Class ini memiliki atribut kelas untuk total pelanggan dan diskon member. Terdapat instance method untuk menampilkan profil dan isi saldo, class method untuk mengubah diskon member global, static method untuk validasi saldo, serta property getter dan setter untuk mengakses atribut private saldo dengan validasi.

class Transaksi: digunakan untuk menyimpan data transaksi berupa ID transaksi otomatis, pelanggan yang membeli, game yang dibeli, dan jumlah pembelian. Class ini memiliki atribut kelas untuk total transaksi dan prefix ID. Terdapat instance method untuk mencetak struk pembelian, class method untuk mendapatkan statistik transaksi, static method untuk menghitung total harga termasuk PPN, serta property getter dan setter untuk mengakses atribut private jumlah_item dengan validasi.

Program menggunakan property setter untuk memvalidasi harga, stok, saldo, dan jumlah pembelian agar tidak menerima nilai yang kurang dari nol atau format yang tidak sesuai. Interaksi antar class dilakukan melalui class Transaksi yang menerima objek Pelanggan dan Game sebagai parameter, kemudian otomatis mengurangi stok game dan saldo pelanggan saat transaksi dibuat.
