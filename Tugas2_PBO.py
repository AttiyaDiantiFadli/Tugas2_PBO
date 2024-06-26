#Membuat Class Mahasiswa
class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_info(self):
        print("Nama Mahasiswa:", self.nama)
        print("NIM:", self.nim)
        print("Jurusan:", self.jurusan.NamaJurusan)
#Penjelasan "Kelas Mahasiswa memiliki atribut nama, nim, dan jurusan,
#serta method tampilkan_info() untuk menampilkan informasi mahasiswa"



#Membuat Class Jurusan
class Jurusan:
    def __init__(self, nama_jurusan):
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.DaftarMahasiswa.append(mahasiswa)

    def tampilkan_daftar_mahasiswa(self):
        print("\nDaftar Mahasiswa di Jurusan", self.NamaJurusan)
        for mahasiswa in self.DaftarMahasiswa:
            print("- Nama:", mahasiswa.nama)
            print("  NIM:", mahasiswa.nim)
#Penjelasan "Kelas Jurusan memiliki atribut nama_jurusan dan DaftarMahasiswa, serta method
#tambah_mahasiswa()untuk menambahkan mahasiswa ke dalam daftar mahasiswa di jurusan tersebut dan
#method tampilkan_daftar_mahasiswa() untuk menampilkan daftar mahasiswa di jurusan tersebut."



#Membuat Class Universitas
class Universitas:
    def __init__(self, nama_universitas):
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = []

    def tambah_jurusan(self, jurusan):
        self.DaftarJurusan.append(jurusan)

    def tampilkan_daftar_jurusan(self):
        print("Daftar Jurusan di Universitas", self.NamaUniversitas)
        for jurusan in self.DaftarJurusan:
            print("- Jurusan:", jurusan.NamaJurusan)
#Penjelasan "Kelas Universitas memiliki atribut nama_universitas dan DaftarJurusan, serta method
#tambah_jurusan() untuk menambahkan jurusan ke dalam daftar jurusan di universitas tersebut dan
#method tampilkan_daftar_jurusan() untuk menampilkan daftar jurusan di universitas tersebut."



#Membuat objek Universitas dengan nama "Universitas Bengkulu"
universitas_xyz = Universitas("Universitas Bengkulu")

#Membuat objek Jurusan dengan nama "Teknik Informatika" dan menambahkannya ke dalam Universitas Bengkulu
jurusan_ti = Jurusan("Teknik Informatika")
universitas_xyz.tambah_jurusan(jurusan_ti)

#Membuat objek Mahasiswa dengan nama, NIM tertentu, dan memasukkannya ke dalam Jurusan Teknik Informatika di Universitas Bengkulu
mahasiswa1 = Mahasiswa("Attiya Dianti Fadli", "G!A022002", jurusan_ti)
mahasiswa2 = Mahasiswa("Merly Yuni Purnama", "G1A022004", jurusan_ti)
mahasiswa3 = Mahasiswa("Tiesya Andriani Ramadhanti", "G1A022014", jurusan_ti)
mahasiswa4 = Mahasiswa("Imelda Cyntia", "G1A022022", jurusan_ti)
jurusan_ti.tambah_mahasiswa(mahasiswa1)
jurusan_ti.tambah_mahasiswa(mahasiswa2)

#Menampilkan daftar jurusan yang ada di Universitas Bengkulu
universitas_xyz.tampilkan_daftar_jurusan()

#Menampilkan daftar mahasiswa yang terdaftar di Jurusan Teknik Informatika di Universitas Bengkulu
jurusan_ti.tampilkan_daftar_mahasiswa()
