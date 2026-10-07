# Sistem Manajemen Toko Game

from datetime import datetime


# class Game 
class Game:
    # atribut kelas
    nama_toko = "toko jaya gemers"
    total_game = 0
    pajak_ppn = 0.11

    def __init__(self, id_game, nama, harga, stok):
        self.__id_game = id_game          
        self.nama = nama                  
        self._harga_dasar = harga         
        self._stok = stok                 
        self.__kode_rahasia = f"SECRET-{id_game}"  #khusus superclass
        Game.total_game += 1

    # encapsulation harga
    @property
    def harga(self):
        return self._harga_dasar

    @harga.setter
    def harga(self, nilai_baru):
        if not isinstance(nilai_baru, (int, float)) or nilai_baru < 0:
            raise ValueError("Harga tidak boleh kurang atau format salah.")
        self._harga_dasar = float(nilai_baru)

    # encapsulation stok
    @property
    def stok(self):
        return self._stok

    @stok.setter
    def stok(self, nilai_baru):
        if not isinstance(nilai_baru, int) or nilai_baru < 0:
            raise ValueError("Stok harus berupa bilangan bulat dan tidak boleh kurang.")
        self._stok = nilai_baru

    @staticmethod
    def cek_valid_harga(nilai):
        try:
            return float(nilai) >= 0
        except (ValueError, TypeError):
            return False

    # class method 
    @classmethod
    def buat_dari_dict(cls, data):
        return cls(data['id'], data['nama'], data['harga'], data['stok'])

    def tambah_stok(self, jumlah):
        if jumlah > 0:
            self._stok += jumlah
            print(f"[INFO] Stok '{self.nama}' berhasil ditambah {jumlah} unit.")
        else:
            print("[ERROR] Jumlah tambah stok harus lebih dari 0.")

    # method ini akan dioverride di subclass
    def tampilkan_info(self):
        print(f"[{self.__id_game}] {self.nama} | Harga: Rp {self._harga_dasar:,.0f} | Stok: {self._stok}")


# subclass GameFisik 
class GameFisik(Game):
    def __init__(self, id_game, nama, harga, stok, kondisi, platform):
        super().__init__(id_game, nama, harga, stok)
        self.kondisi = kondisi          
        self.platform = platform        

    # override method dari superclass
    def tampilkan_info(self):
        print(f"[Game FISIK] {self.nama} | Platform: {self.platform} | "
              f"Kondisi: {self.kondisi} | Harga: Rp {self._harga_dasar:,.0f} | Stok: {self._stok}")

    def hitung_harga_final(self):
        if self.kondisi == "Bekas":
            return self._harga_dasar * 0.7
        return self._harga_dasar


# subclass GameDigital
class GameDigital(Game):
    def __init__(self, id_game, nama, harga, stok, kode_download, ukuran_file):
        super().__init__(id_game, nama, harga, stok)
        self.kode_download = kode_download      
        self.ukuran_file = ukuran_file          

    # override method dari superclass
    def tampilkan_info(self):
        print(f"[Game DIGITAL] {self.nama} | Kode: {self.kode_download} | "
              f"Ukuran: {self.ukuran_file}GB | Harga: Rp {self._harga_dasar:,.0f} | Stok: {self._stok}")

    def hitung_harga_final(self):
        return self._harga_dasar * 1.05


class Pelanggan:
    total_pelanggan = 0
    diskon_member = 0.05

    def __init__(self, id_pelanggan, nama, saldo):
        self.__id_pelanggan = id_pelanggan  
        self.nama = nama                    
        self.saldo = saldo
        Pelanggan.total_pelanggan += 1

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, nilai_baru):
        if not isinstance(nilai_baru, (int, float)) or nilai_baru < 0:
            raise ValueError("Saldo tidak boleh kurang atau format salah.")
        self.__saldo = float(nilai_baru)

    @staticmethod
    def cek_valid_saldo(nilai):
        try:
            return float(nilai) >= 0
        except (ValueError, TypeError):
            return False

    @classmethod
    def ubah_diskon_global(cls, diskon_baru):
        if 0 <= diskon_baru <= 1:
            cls.diskon_member = diskon_baru
            print(f"[INFO] Diskon member global diubah menjadi {cls.diskon_member * 100:.0f}%")
        else:
            print("[ERROR] Diskon harus antara 0 dan 1.")

    def isi_saldo(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah
            print(f"[INFO] Isi saldo berhasil. Saldo {self.nama}: Rp {self.saldo:,.0f}")
        else:
            print("[ERROR] Jumlah isi saldo harus lebih dari 0.")

    def tampilkan_info(self):
        print(f"[{self.__id_pelanggan}] {self.nama} | Saldo: Rp {self.saldo:,.0f}")

# class Toko 
class Toko:
    def __init__(self, nama_toko, alamat):
        self.nama_toko = nama_toko
        self.alamat = alamat
        self._daftar_pelanggan = []     

    def tambah_pelanggan(self, pelanggan):
        if isinstance(pelanggan, Pelanggan):
            self._daftar_pelanggan.append(pelanggan)
            print(f"[INFO] {pelanggan.nama} terdaftar di {self.nama_toko}")

    def tampilkan_daftar_pelanggan(self):
        print(f"\n=== Daftar Pelanggan {self.nama_toko} ===")
        if not self._daftar_pelanggan:
            print("Belum ada pelanggan terdaftar.")
            return
        for p in self._daftar_pelanggan:
            p.tampilkan_info()


# class DetailTransaksi 
class DetailTransaksi:
    def __init__(self, game, jumlah):
        self.game = game
        self.jumlah = jumlah
        self.subtotal = game.harga * jumlah

    def tampilkan_detail(self):
        print(f"  - {self.game.nama} x{self.jumlah} = Rp {self.subtotal:,.0f}")


# class Transaksi
class Transaksi:
    total_transaksi = 0
    prefix_id = "TRX"

    def __init__(self, pelanggan, game, jumlah_item):
        Transaksi.total_transaksi += 1
        self.__id_transaksi = f"{Transaksi.prefix_id}-{Transaksi.total_transaksi:04d}"
        self.tanggal = datetime.now().strftime("%d-%m-%Y %H:%M")

        # Asosiasi
        self.pelanggan = pelanggan
        self.game = game

        # Komposisi
        self.__detail = DetailTransaksi(game, jumlah_item)

        self.__total_bayar = self.hitung_total(game.harga, jumlah_item, Game.pajak_ppn)

        self.game.stok -= jumlah_item
        self.pelanggan.saldo -= self.__total_bayar

    @property
    def jumlah_item(self):
        return self.__detail.jumlah

    @staticmethod
    def hitung_total(harga, qty, pajak):
        subtotal = harga * qty
        return subtotal + (subtotal * pajak)

    @classmethod
    def get_statistik(cls):
        return f"Total transaksi tercatat: {cls.total_transaksi}"

    def cetak_struk(self):
        print("\n" + "=" * 50)
        print(f"  STRUK PEMBELIAN - {Game.nama_toko}")
        print("=" * 50)
        print(f"ID Transaksi : {self.__id_transaksi}")
        print(f"Tanggal      : {self.tanggal}")
        print(f"Pelanggan    : {self.pelanggan.nama}")
        print("Detail Item:")
        self.__detail.tampilkan_detail()
        pajak_amount = self.game.harga * self.__detail.jumlah * Game.pajak_ppn
        print(f"PPN ({Game.pajak_ppn * 100:.0f}%)      : Rp {pajak_amount:,.0f}")
        print(f"TOTAL BAYAR  : Rp {self.__total_bayar:,.0f}")
        print("=" * 50)
        print(f"Sisa Saldo   : Rp {self.pelanggan.saldo:,.0f}")
        print("=" * 50 + "\n")


# bagian pengujian program
if __name__ == "__main__":
    print("====== SISTEM MANAJEMEN TOKO GAME ======\n")

    # data gamenya
    game_fisik1 = GameFisik("GF001", "Elden Ring", 599000, 10, "Baru", "PS5")
    game_fisik2 = GameFisik("GF002", "FIFA 25", 799000, 5, "Bekas", "PS5")
    game_digital1 = GameDigital("GD001", "Hollow Knight", 150000, 25, "HK-REDEEM-001", 2.5)
    game_digital2 = GameDigital("GD002", "Stardew Valley", 120000, 30, "SV-REDEEM-002", 1.2)

    daftar_game = [game_fisik1, game_fisik2, game_digital1, game_digital2]
    for g in daftar_game:
        g.tampilkan_info()

    print(f"\nTotal game terdaftar: {Game.total_game}")

    # coba method dari subclass
    print("\n----- Coba Method Subclass -----")
    print(f"Harga final Elden Ring (Baru): Rp {game_fisik1.hitung_harga_final():,.0f}")
    print(f"Harga final FIFA 25 (Bekas): Rp {game_fisik2.hitung_harga_final():,.0f}")
    print(f"Harga final Hollow Knight (Digital): Rp {game_digital1.hitung_harga_final():,.0f}")
    print(f"Harga final Stardew Valley (Digital): Rp {game_digital2.hitung_harga_final():,.0f}")

    print(f"\nApakah game_fisik1 instance dari Game? {isinstance(game_fisik1, Game)}")
    print(f"Apakah GameFisik subclass dari Game? {issubclass(GameFisik, Game)}")

    # data pelanggannya
    print("\n----- Data Pelanggan -----")
    pelanggan1 = Pelanggan("P001", "suhri", 2000000)
    pelanggan2 = Pelanggan("P002", "udin", 1500000)

    daftar_pelanggan = [pelanggan1, pelanggan2]
    for p in daftar_pelanggan:
        p.tampilkan_info()

    # toko nampung pelanggan
    print("\n----- Toko dan Pelanggan -----")
    toko = Toko("toko jaya gemers", "Samarinda")
    toko.tambah_pelanggan(pelanggan1)
    toko.tambah_pelanggan(pelanggan2)
    toko.tampilkan_daftar_pelanggan()

    print("\n(Bukti agregasi: pelanggan tetap hidup mandiri)")
    pelanggan1.tampilkan_info()

    # proses belinya
    print("\n----- Proses Transaksi -----")
    trx1 = Transaksi(pelanggan1, game_fisik1, 1)
    trx1.cetak_struk()

    # coba setter
    print("----- Uji Setter -----")
    try:
        print("Mencoba ubah harga game_fisik1 ke 650000 (Valid)...")
        game_fisik1.harga = 650000
        print(f"Berhasil. Harga baru: Rp {game_fisik1.harga:,.0f}")
    except ValueError as e:
        print(e)

    try:
        print("Mencoba ubah stok game_digital1 ke -5 (Tidak Valid)...")
        game_digital1.stok = -5
    except ValueError as e:
        print(f"Gagal: {e}")

    try:
        print("Mencoba isi saldo pelanggan2 dengan teks (Tidak Valid)...")
        pelanggan2.saldo = "dua ratus ribu"
    except ValueError as e:
        print(f"Gagal: {e}")

    # transaksi kedua
    print("\n----- Transaksi Game Digital -----")
    trx2 = Transaksi(pelanggan2, game_digital1, 2)
    trx2.cetak_struk()

    # cek hasil akhir
    print("----- Final State -----")
    for g in daftar_game:
        g.tampilkan_info()
    print()
    print(Transaksi.get_statistik())
    print("\nProgram selesai.")