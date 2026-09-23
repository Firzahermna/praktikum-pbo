# Sistem Manajemen Toko Game

class Game:
    # Atribut kelas - dimiliki bersama oleh semua objek Game
    nama_toko = "toko jaya gemers"
    total_game = 0
    pajak_ppn = 0.11

    def __init__(self, id_game, nama, harga, stok):
        # Atribut instance - unik untuk tiap objek
        self.__id_game = id_game      # private
        self.nama = nama              # public
        self.harga = harga
        self.stok = stok
        Game.total_game += 1

    # Encapsulation untuk atribut harga
    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, nilai_baru):
        if not isinstance(nilai_baru, (int, float)) or nilai_baru < 0:
            raise ValueError("Harga tidak boleh kurang atau format salah.")
        self.__harga = float(nilai_baru)

    # Encapsulation untuk atribut stok
    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, nilai_baru):
        if not isinstance(nilai_baru, int) or nilai_baru < 0:
            raise ValueError("Stok harus berupa bilangan bulat dan tidak boleh kurang.")
        self.__stok = nilai_baru

    # Validasi apakah harga valid
    @staticmethod
    def cek_valid_harga(nilai):
        try:
            return float(nilai) >= 0
        except (ValueError, TypeError):
            return False

    # membuat objek game dari dictionary
    @classmethod
    def buat_dari_dict(cls, data):
        return cls(data['id'], data['nama'], data['harga'], data['stok'])

    def tambah_stok(self, jumlah):
        if jumlah > 0:
            self.stok += jumlah
            print(f"[INFO] Stok '{self.nama}' berhasil ditambah {jumlah} unit.")
        else:
            print("[ERROR] Jumlah tambah stok harus lebih dari 0.")

    def tampilkan_info(self):
        print(f"[{self.__id_game}] {self.nama} | Harga: Rp {self.harga:,.0f} | Stok: {self.stok}")


class Pelanggan:
    total_pelanggan = 0
    diskon_member = 0.05

    def __init__(self, id_pelanggan, nama, saldo):
        self.__id_pelanggan = id_pelanggan  # privat
        self.nama = nama                    # publik
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

    # Class method untuk mengubah atribut kelas
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


class Transaksi:
    total_transaksi = 0
    prefix_id = "TRX"

    def __init__(self, pelanggan, game, jumlah_item):
        Transaksi.total_transaksi += 1
        self.__id_transaksi = f"{Transaksi.prefix_id}-{Transaksi.total_transaksi:04d}"
        
        self.pelanggan = pelanggan
        self.game = game
        self.jumlah_item = jumlah_item

        self.__total_bayar = self.hitung_total(game.harga, jumlah_item, Game.pajak_ppn)

        # bagian transaksi kurangi stok game & saldo pelanggan
        self.game.stok -= jumlah_item
        self.pelanggan.saldo -= self.__total_bayar

    @property
    def jumlah_item(self):
        return self.__jumlah_item

    @jumlah_item.setter
    def jumlah_item(self, nilai_baru):
        if not isinstance(nilai_baru, int) or nilai_baru <= 0:
            raise ValueError("Jumlah item harus bilangan bulat nol.")
        self.__jumlah_item = nilai_baru

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
        print(f"Pelanggan    : {self.pelanggan.nama}")
        print(f"Item         : {self.game.nama}")
        print(f"Jumlah       : {self.jumlah_item} unit")
        print(f"Harga Satuan : Rp {self.game.harga:,.0f}")
        pajak_amount = self.game.harga * self.jumlah_item * Game.pajak_ppn
        print(f"PPN ({Game.pajak_ppn * 100:.0f}%)      : Rp {pajak_amount:,.0f}")
        print(f"TOTAL BAYAR  : Rp {self.__total_bayar:,.0f}")
        print("=" * 50)
        print(f"Sisa Saldo   : Rp {self.pelanggan.saldo:,.0f}")
        print("=" * 50 + "\n")


# Bagian pengujian program
if __name__ == "__main__":
    print("====== DEMONSTRASI SISTEM MANAJEMEN TOKO GAME ======\n")

    # Setup data awal
    game1 = Game("G001", "Elden Ring", 599000, 10)
    game2 = Game.buat_dari_dict({"id": "G002", "nama": "Hollow Knight", "harga": 150000, "stok": 25})
    
    pelanggan1 = Pelanggan("P001", "suhri", 1000000)
    pelanggan2 = Pelanggan("P002", "udin", 500000)

    # Uji method objek
    game1.tampilkan_info()
    game1.tambah_stok(5)
    pelanggan1.isi_saldo(500000)

    #  Uji class method
    Pelanggan.ubah_diskon_global(0.10)
    print(Transaksi.get_statistik())

    # Demo static method
    print(f"Validasi harga -100: {Game.cek_valid_harga(-100)}")
    print(f"Validasi harga 50000: {Game.cek_valid_harga(50000)}")

    # Validasi data
    print("\n--- Uji Setter ---")
    try:
        print("Mencoba ubah harga ke 650000 (Valid)...")
        game1.harga = 650000
        print(f"Berhasil. Harga baru: Rp {game1.harga:,.0f}")
    except ValueError as e:
        print(e)

    try:
        print("Mencoba ubah stok ke -5 (Tidak Valid)...")
        game1.stok = -5
    except ValueError as e:
        print(f"Gagal: {e}")

    try:
        print("Mencoba isi saldo dengan teks (Tidak Valid)...")
        pelanggan2.saldo = "dua ratus ribu"
    except ValueError as e:
        print(f"Gagal: {e}")

    # Demo transaksi
    print("\n--- Proses Transaksi ---")
    trx1 = Transaksi(pelanggan1, game1, 1)
    trx1.cetak_struk()

    # Final check
    print("--- Final State ---")
    game1.tampilkan_info()
    print(Transaksi.get_statistik())
