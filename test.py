from frauddetection import FakeNewsDetector

# Contoh teks berita palsu yang tersebar di sosial media untuk pengujian 
text1 = """Gaji Presiden RI mencengangkan dikabarkan bakal mengalami kenaikan. 
            bagikan segera sebelum terlambat!"""
text2 = """DIBUKA LOWONGAN PETUGAS HAJI INDONESIA, SEGERA DAFTARKAN DIRI ANDA 
            PENDAFTARAN TERBATAS !!!"""
text3 = """Penemuan mengejutkan di Hutan HujanAmazon! Tengkorak Raksasa dengan 
            leher terpanjang didunia,"""
text4 = """ SIAP-SIAP! Pemegang Kartu KIS BPJS Kesehatan Bakalan Terima 3 Bansos 
            Pada Oktober 2024.
            Untuk menjamin kesehatan masyarakat kategori miskin, pemegang Kartu 
            Indonesia Sehat (KIS) BPJS 
            Kesehatan dipastikan menerima sejumlah bansos penting dari pemerintah.
            untuk mendapatkan bantukan langsung klik daftar"""
text5 = """BANSOS PKH 2024 Bantuan Sosial uang tunai
           Akhirnya sudah ada informasi jelas hari ini, ada bantuan bansos yang mau 
           dapat bantuan bansos 
           silahkan daftar link 👇👇👇
           https://xxbansos2024.pdjhc.store/"""
text6 = "Ma'ruf amin: kalau jokowi terpilih lagi 3 periode ibu-ibu cukup bayar pakai kartu"
text7 = """Mulai besok dan seterusnya ada peraturan komunikasi baru.
            Setelah dilantikn ya Badan Siber & Sandi Nasional (BSSN), oleh Bpk Jokowi , 
            Presiden NKRI:
            .Semua panggilan dicatat.
            .Semua rekaman panggilan telepon tersimpan.
            .WhatsApp dipantau,
            .Twitter dipantau,
            .Facebook dipantau,
            Semua....media sosial..... dan forum dimonitor,
            Informasikan kepada mereka yang tidak tahu.
            Perangkat Anda terhubung ke sistem pelayanan.
            Berhati-hatilah mengirimkan pesan yg tidak perlu.
            Beritahu anak-anak Anda, Kerabat dan teman tentang berita ini
            Jangan teruskan tulisan atau video dll,
            Polisi telah mengeluarkan pemberitahuan yang disebut .. Kejahatan
            Cargo ... dan tindakan akan dilakukan ... bila perlu hapus saja.
            Menulis atau meneruskan pesan apapun pada setiap perdebatan politik dan agama 
            Informasikan berita ini kepada orang lain agar selalu waspada.
            Ini sangat serius, perlu diketahui semua kelompok dan anggota /individu."""

# Inisialisasi objek FakeNewsDetector
detector = FakeNewsDetector()
hasil1 = detector.classify(text1)
print(hasil1[0])
hasil2 = detector.classify(text2)
print(hasil2[0])
hasil3 = detector.classify(text3)
print(hasil3[0])
hasil4 = detector.classify(text4)
print(hasil4[0])
hasil5 = detector.classify(text5)
print(hasil5[0])
hasil6 = detector.classify(text6)
print(hasil6[0])
hasil7 = detector.classify(text7)
print(hasil7[0])
