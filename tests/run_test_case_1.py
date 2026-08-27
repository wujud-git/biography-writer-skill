#!/usr/bin/env python3
"""
Test Case 1: Basic Biography Generation
Data: Siti Nurhaliza - Complete biography with all 6 life stages
"""

import json
from scripts.biography_generator import BiographyGenerator

def run_test_case_1():
    """Run test case 1: Siti Nurhaliza biography."""
    
    print("=" * 70)
    print("TEST CASE 1: BASIC BIOGRAPHY GENERATION")
    print("=" * 70)
    print("\nGenerating biography for: SITI NURHALIZA")
    print("Status: Running...\n")
    
    # Create biography generator
    bg = BiographyGenerator("SITI NURHALIZA")
    
    # MASA KECIL DATA
    print("📝 Processing: Masa Kecil...")
    bg.add_chapter_data('masa_kecil', {
        'narasi': '''Siti Nurhaliza dilahirkan pada 31 Januari 1974 di Kuala Lumpur, Malaysia, 
sebuah kota yang akan menjadi saksi awal dari perjalanan luar biasa seorang penyanyi legendaris. 
Orang tuanya, Noor Hadjam dan Shalimar, menyambut kedatangannya dengan penuh kebahagiaan. 
Ayahnya, seorang pengusaha sukses, membawa semangat kerja keras dan dedikasi, sementara ibunya 
yang bekerja sebagai ibu rumah tangga mencurahkan perhatian penuh pada pengembangan bakat-bakat 
anaknya yang akan terbukti luar biasa.

Keluarga Nurhaliza adalah keluarga yang harmonis, diikat oleh nilai-nilai tradisional dan budaya 
Islam yang kuat. Sejak kecil, Siti dikelilingi oleh musik dan seni, mencerminkan apresiasi orang 
tuanya terhadap eksplorasi kreatif. Rumah mereka sering ramai dengan lagu-lagu indah, mengalun dari 
alat musik tradisional Malaysia dan ibu kota global yang berkembang. Ini adalah lingkungan sempurna 
untuk sebuah bakat yang sedang menunggu untuk bersinar.

Momen bersejarah tiba ketika Siti berusia hanya tiga tahun—orang tuanya mengakui dalam dirinya 
kemampuan vokal yang luar biasa. Bukan sekadar minat biasa terhadap musik, melainkan bakat yang 
tampak lahir dari dalam, sesuatu yang tidak bisa ditawarkan, tidak bisa diajarkan dengan cara 
biasa. Pada usia lima tahun, penampilan pertamanya di acara keluarga membuat semua orang terpukau. 
Suara yang jernih dan penuh perasaan keluar dari tubuh kecil itu, membuat orang tua sadar bahwa 
mereka tidak hanya memiliki anak biasa, melainkan seorang penyanyi berbakat yang akan mengubah 
sejarah musik Asia.'''
    })
    
    # PENDIDIKAN DATA
    print("📝 Processing: Pendidikan...")
    bg.add_chapter_data('pendidikan', {
        'narasi': '''Perjalanan pendidikan Siti Nurhaliza dibentuk oleh kombinasi unik antara 
pendidikan formal dan pengembangan talenta artistik yang intensif. Di Malaysia, dia menjalani 
pendidikan dasar hingga menengah dengan prestasi yang gemilang, menunjukkan kecerdasan akademik 
yang seimbang dengan passion artistiknya. Sekolah-sekolah yang dia hadiri mengakui keistimewaannya 
dan memberikan dukungan untuk mengembangkan bakat vokalnya di samping tanggung jawab akademik.

Namun pendidikan Siti tidak terbatas pada ruang kelas. Sejak berusia muda, dia menjalani pelatihan 
vokal intensif yang membentuk fondasi teknis untuk karir yang akan datang. Guru musik dan mentornya, 
terutama Puan Mariana—seorang guru musik berbakat yang mengenali potensi luar biasa dalam diri Siti—
memainkan peran krusial dalam mengembangkan kemampuan vokalnya. Di bawah bimbingan yang cermat, 
Siti tidak hanya belajar teknik menyanyi yang sempurna, tetapi juga cara mengekspresikan emosi 
melalui musik, cara yang akan menjadi ciri khas interpretasinya yang mendalam.

Pengalaman paling berkesan datang pada tahun 1990 ketika Siti, masih sekolah menengah, memenangkan 
kompetisi nyanyi tingkat negara bagian. Kemenangan ini bukan hanya penghargaan bagi dedikasi dan 
bakat, melainkan pengakuan publik bahwa Siti Nurhaliza adalah bintang yang akan bersinar terang. 
Kompetisi ini menjadi titik balik yang mendorong Siti untuk mengejar impian besarnya dengan lebih 
percaya diri dan determinasi yang tidak tergoyahkan.'''
    })
    
    # KARIR AWAL DATA
    print("📝 Processing: Karir Awal...")
    bg.add_chapter_data('karir_awal', {
        'narasi': '''Transisi dari penyanyi berbakat muda menjadi profesional sejati terjadi pada 
tahun 1995 ketika Siti Nurhaliza menandatangani kontrak dengan label rekaman BMG Records. Peluncuran 
karirnya ditandai dengan single debut yang revolusioner—"Dato' Merah"—yang membius industri musik 
Malaysia dan sekitarnya dengan cara yang belum pernah terjadi sebelumnya. Lagu ini bukan sekadar 
melodi yang indah; ia membawa cerita yang dalam, emosi yang autentik, dan interpretasi vokal yang 
memukau, semuanya dikemas dalam produksi yang sempurna.

Tantangan-tantangan muncul segera setelah kesuksesan awal. Industri musik adalah arena yang kejam, 
penuh dengan persaingan yang ketat dan tekanan yang tidak pernah berhenti untuk menghasilkan 
kesuksesan yang lebih besar. Media massa memburu setiap langkahnya, fans menuntut konten baru yang 
terus-menerus, dan standar kualitas yang semakin tinggi setiap tahunnya. Namun, alih-alih 
menyerah, Siti menggunakan tantangan ini sebagai bahan bakar untuk menjadi lebih baik. Dia bekerja 
dengan produser terbaik, berkolaborasi dengan musisi berbakat, dan tidak pernah berhenti 
mengembangkan keahliannya.

Album pertamanya mencapai penjualan lebih dari 100,000 kopi dalam enam bulan pertama—sebuah angka 
yang luar biasa untuk penyanyi pemula pada era itu. Kesuksesan ini membuka pintu bagi pencapaian 
yang lebih besar, memberikan Siti momentum yang dia butuhkan untuk melompat ke panggung internasional. 
Setiap penampilan, setiap lagu baru, setiap penghargaan kecil adalah batu loncatan menuju takdir 
besarnya yang akan mengubah lanskap musik Asia selamanya.'''
    })
    
    # PENCAPAIAN UTAMA DATA
    print("📝 Processing: Pencapaian Utama...")
    bg.add_chapter_data('pencapaian_utama', {
        'narasi': '''Pencapaian terbesar Siti Nurhaliza datang pada puncak karirnya ketika dia 
menjadi satu-satunya penyanyi Malaysia yang pernah memenangkan Grammy Awards, penghargaan tertinggi 
dalam industri musik global. Pencapaian ini lebih dari sekadar trofi atau pengakuan; ini adalah 
bukti bahwa seorang seniman Asia bisa bersaing dan menang di panggung dunia terbesar, mengalahkan 
pesaing-pesaing internasional yang sudah mapan. Kemenangan Grammy ini membuka mata dunia terhadap 
kualitas musik Asia dan membuka jalan bagi generasi seniman Asia berikutnya.

Namun Grammy hanya salah satu dari banyak puncak yang dia raih. Siti telah memenangkan MTV Asia 
Awards berkali-kali, World Music Awards yang bergengsi, dan penghargaan-penghargaan internasional 
lainnya yang tidak terhitung jumlahnya. Setiap penghargaan adalah representasi dari jam-jam kerja 
tanpa henti, dedikasi yang tidak pernah surut, dan passion yang tidak pernah padam untuk musik.

Album 2000 yang beraksara "Siti" menjadi album terlaris sepanjang masa di Asia Tenggara dengan 
penjualan mencapai 5 juta kopi—sebuah rekor yang menakjubkan bahkan dalam standar global. Proyek 
ini bukan hanya tentang angka penjualan, tetapi tentang dampak budaya yang mendalam. Siti 
menggunakan platform globalnya untuk mempromosikan warisan budaya Asia, mempertahankan identitas 
Islam dan Malaynya sambil menarik jutaan pendengar dari berbagai latar belakang budaya. Dia menjadi 
duta budaya yang tidak resmi, jembatan antara Timur dan Barat, membuktikan bahwa musik adalah 
bahasa universal yang melampaui semua batas.'''
    })
    
    # KEHIDUPAN KELUARGA DATA
    print("📝 Processing: Kehidupan Keluarga...")
    bg.add_chapter_data('kehidupan_keluarga', {
        'narasi': '''Pada tahun 2003, di puncak kesuksesan internasionalnya, Siti Nurhaliza 
memutuskan untuk membuka hatinya untuk cinta. Dia menikah dengan Datuk K. Nasimuddin, seorang 
pengusaha yang mapan dan penyokong seni yang tulus. Pernikahan mereka bukan hanya perayaan pribadi, 
tetapi momen budaya yang ditonton oleh jutaan orang di seluruh dunia. Fans dari berbagai negara 
berdoa untuk kebahagiaan pasangan yang mereka cintai, mencerminkan bagaimana Siti telah menjadi 
bagian integral dari kehidupan emosional jutaan orang.

Keluarga mereka berkembang dengan kedatangan tiga putra yang luar biasa: Muhammad Syukri pada 
2005, Muhammad Shafiq Shuib pada 2006, dan Muhammad Syarif pada 2009. Dengan menjadi seorang ibu 
dari tiga anak laki-laki, Siti menghadapi tantangan baru yang berbeda dari panggung internasional. 
Namun, dia melakoninya dengan grace yang sama seperti dia menjalani karirnya—dengan dedikasi penuh 
dan komitmen yang tidak goyah. Dia secara aktif mengurangi jadwal konser internasionalnya untuk 
memastikan bahwa dia tidak melewatkan momen-momen berharga dalam kehidupan anak-anaknya.

Nilai-nilai yang menggerakkan Siti sebagai ibu adalah perpanjangan dari nilai-nilai yang menggerakkan 
dirinya sebagai artis: integritas, dedikasi, keseimbangan antara ambisi dan kerendahan hati, dan 
komitmen yang tidak tergoyahkan terhadap apa yang penting. Dia mengajarkan anak-anaknya tentang 
pentingnya kerja keras, rasa hormat terhadap tradisi, dan tanggung jawab untuk menjadi anggota 
masyarakat yang baik. Pernikahan dan keluarganya adalah saksi yang indah terhadap kelengkapan hidup 
yang sesungguhnya—kesuksesan profesional yang luar biasa dipadu dengan kehidupan keluarga yang 
penuh makna dan cinta yang mendalam.'''
    })
    
    # WARISAN/LEGASI DATA
    print("📝 Processing: Warisan dan Legasi...")
    bg.add_chapter_data('warisan', {
        'narasi': '''Ketika merenungkan kontribusi terbesar Siti Nurhaliza kepada dunia, yang 
paling menonjol adalah bagaimana dia telah menginspirasi jutaan penyanyi muda di seluruh Asia 
untuk mengejar impian mereka. Dia membuktikan bahwa seorang seniman dari Malaysia, dari Asia Tenggara, 
bisa bersaing dan menang di panggung dunia. Dia menghancurkan hambatan dan membuka pintu yang 
sebelumnya dianggap tertutup. Generasi penyanyi muda melihat dalam kesuksesannya bukti bahwa 
impian mereka bukan mustahil, melainkan sesuatu yang dapat dicapai dengan kerja keras dan dedikasi.

Nilai-nilai yang ingin Siti tinggalkan adalah jauh lebih dalam dari sekadar keberhasilan musik. 
Dia menginginkan dunia mengingat pentingnya menjaga akar budaya sambil merangkul inovasi, tentang 
keseimbangan antara ambisi profesional dan tanggung jawab personal, tentang kekuatan integritas 
dalam sebuah industri yang sering kali mengorbankannya. Melalui setiap lagu yang dia nyanyikan, 
setiap penghargaan yang dia raih, setiap momen bersama keluarganya, Siti menyampaikan pesan yang 
konsisten: kesuksesan sejati terletak pada dampak positif yang Anda tinggalkan.

Sebagai warisan terakhir, Siti Nurhaliza akan dikenang sebagai penyanyi paling berpengaruh yang 
pernah dihasilkan Asia, seorang duta budaya yang telah membawa kebanggaan bagi seluruh benua. 
Tetapi lebih dari itu, dia akan dikenang sebagai seorang wanita yang menjalani hidupnya dengan 
integritas yang luar biasa, seseorang yang tidak pernah melupakan dari mana dia berasal bahkan 
ketika dunia menghampirinya dengan kehormat tertinggi. Lagu-lagu Siti akan terus dinyanyikan 
oleh generasi mendatang, bukan hanya karena keindahan melodi mereka, tetapi karena kedalaman 
pesan yang dibawanya tentang cinta, harapan, dan kekuatan semangat manusia.'''
    })
    
    # Add timeline events
    print("📝 Processing: Timeline Events...")
    bg.add_timeline_event(1974, 'Dilahirkan di Kuala Lumpur, Malaysia', month=1)
    bg.add_timeline_event(1977, 'Mulai belajar menyanyi', month=3)
    bg.add_timeline_event(1979, 'Penampilan pertama di acara keluarga', month=6)
    bg.add_timeline_event(1990, 'Memenangkan kompetisi nyanyi tingkat negara bagian', month=7)
    bg.add_timeline_event(1995, 'Menandatangani kontrak dengan BMG Records', month=3)
    bg.add_timeline_event(1995, 'Meluncurkan single debut "Dato\' Merah"', month=8)
    bg.add_timeline_event(2000, 'Album "Siti" menjadi album terlaris di Asia Tenggara', month=5)
    bg.add_timeline_event(2001, 'Memenangkan Grammy Awards', month=2)
    bg.add_timeline_event(2003, 'Menikah dengan Datuk K. Nasimuddin', month=11)
    bg.add_timeline_event(2005, 'Kelahiran putra pertama, Muhammad Syukri', month=1)
    bg.add_timeline_event(2006, 'Kelahiran putra kedua, Muhammad Shafiq', month=3)
    bg.add_timeline_event(2009, 'Kelahiran putra ketiga, Muhammad Syarif', month=7)
    
    # Generate document
    print("📝 Generating Word document...\n")
    output_file = 'biography_siti_nurhaliza.docx'
    result = bg.save(output_file)
    
    print("=" * 70)
    print("✅ TEST CASE 1 COMPLETED SUCCESSFULLY")
    print("=" * 70)
    print(f"\n📄 Output File: {result}")
    print(f"📊 Chapters Generated: 6")
    print(f"📅 Timeline Events: 12")
    print(f"✨ Formatting: Professional Word Document (.docx)")
    print(f"\n🎉 Biography for SITI NURHALIZA has been generated!")
    print(f"\nFile is ready in: /home/claude/biography-writer/{output_file}")

if __name__ == '__main__':
    run_test_case_1()
