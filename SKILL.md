---
name: biography-writer
description: Transform raw data and facts into a beautifully structured biographical book with photos, table of contents, and interactive timeline. Use this skill whenever someone needs to convert biographical information into a polished Word document (.docx) biography organized by 6 life stages (Masa Kecil, Pendidikan, Karir Awal, Pencapaian Utama, Kehidupan Keluarga, Warisan/Legasi). The skill uses an interactive guided interview to extract comprehensive details, automatically generates semi-formal narrative chapters with 3-5 paragraphs each, adds photos where provided, creates automatic table of contents, and includes an interactive timeline or sidebar for visual chronology. Perfect for creating personal memoirs, professional biographies, family histories, or legacy documents.
compatibility: Python 3.8+, python-docx library, Pillow (untuk image handling)
---

# Biography Writer Skill

Transform biographical data into a beautifully structured book with chapters, photos, table of contents, and interactive timeline.

## What This Skill Does

The Biography Writer skill provides an **interactive guided experience** that:

- **Asks targeted questions**: Guides you through a structured interview for each life stage
- **Organizes into 6 chapters**: Masa Kecil → Pendidikan → Karir Awal → Pencapaian Utama → Kehidupan Keluarga → Warisan/Legasi
- **Creates narrative chapters**: Converts your answers into semi-formal, flowing 3-5 paragraph chapters
- **Adds photos**: Integrates images at relevant points throughout the biography
- **Generates Table of Contents**: Professional auto-generated TOC with page numbers
- **Includes Timeline/Sidebar**: Visual chronological representation of key life events
- **Professional formatting**: Publication-ready Word document (.docx) suitable for printing

## How to Use This Skill

The Biography Writer uses an **interactive guided interview approach**. Simply tell me you want to create a biography, and I'll lead you through a structured conversation.

### Workflow Interaktif (Interactive Workflow)

**Step 1: Perkenalan (Introduction)**
```
Saya: "Mari kita buat biografi yang menakjubkan! Siapa nama lengkap orang yang akan kita ceritakan?"
Anda: "John Doe"
```

**Step 2: Interview per Tahapan (Stage-by-Stage Interview)**

Untuk setiap tahapan kehidupan, saya akan bertanya pertanyaan yang spesifik:

#### MASA KECIL (Early Life)
- Kapan dan di mana lahir?
- Siapa nama orang tua?
- Bagaimana kondisi keluarga pada saat itu?
- Peristiwa penting apa di masa kecil?
- Ada foto masa kecil? (optional)

#### PENDIDIKAN (Education)
- Sekolah mana yang dihadiri?
- Prestasi akademik apa yang dicapai?
- Guru atau mentor berpengaruh?
- Pengalaman berkesan di sekolah?
- Ada foto dari masa sekolah? (optional)

#### KARIR AWAL (Early Career)
- Pekerjaan pertama apa?
- Kapan memulai?
- Tantangan apa yang dihadapi?
- Pencapaian pertama yang berarti?

#### PENCAPAIAN UTAMA (Major Achievements)
- Apa pencapaian terbesar?
- Penghargaan atau pengakuan?
- Proyek atau inisiatif penting?
- Dampak apa yang dihasilkan?
- Foto atau dokumentasi pencapaian? (optional)

#### KEHIDUPAN KELUARGA (Family Life)
- Pernikahan atau hubungan penting?
- Anak-anak?
- Nilai-nilai keluarga?
- Keseimbangan kerja dan keluarga?
- Momen keluarga berkesan?

#### WARISAN/LEGASI (Legacy)
- Apa kontribusi terbesar Anda?
- Nilai atau pesan apa yang ingin ditinggalkan?
- Bagaimana orang lain mengingat Anda?
- Rencana atau impian masa depan?

**Step 3: Photo Upload (Optional)**
```
Untuk setiap tahapan, Anda bisa upload foto. Saya akan:
- Validasi dan resize foto
- Menempatkan di lokasi yang relevan dalam dokumen
- Memberikan caption otomatis
```

**Step 4: Timeline/Sidebar Data**
Saya akan secara otomatis mengumpulkan:
- Tanggal-tanggal penting
- Milestone (pencapaian penting)
- Lokasi-lokasi signifikan
Untuk membuat timeline visual atau sidebar

**Step 5: Document Generation**
Setelah semua informasi terkumpul, saya akan:
1. Menulis narasi 3-5 paragraf untuk setiap bab
2. Memasukkan foto di tempat yang tepat
3. Membuat Daftar Isi otomatis
4. Membuat Timeline/Sidebar visual
5. Generate dokumen Word profesional

### Output

Anda akan menerima file `.docx` yang berisi:
- ✅ Halaman Judul dengan nama dan foto
- ✅ Daftar Isi (auto-generated)
- ✅ 6 Bab dengan narasi semi-formal
- ✅ Foto yang terintegrasi di setiap bab relevan
- ✅ Timeline atau sidebar visual
- ✅ Formatting profesional, siap cetak

## Best Practices untuk Hasil Terbaik

### Saat Menjawab Pertanyaan

1. **Be specific**: Jangan hanya "saya lahir di Jakarta". Lebih baik: "Saya lahir di Jakarta, tepatnya di Rumah Sakit Pondok Indah, pada hari Jumat pagi jam 6 pagi di tengah hujan deras"
2. **Include emotions**: Ceritakan perasaan Anda, bukan hanya fakta
3. **Add stories**: Anekdot kecil membuat biografi lebih hidup
4. **Mention people**: Nama orang yang berpengaruh membantu narasi

### Tentang Foto/Gambar

- **Jenis file**: JPG, PNG (ukuran ideal: 2-5MB per foto)
- **Jumlah**: Rekomendasikan 1-2 foto per bab (total 6-12 foto)
- **Kualitas**: Foto yang jelas dan bersejarah lebih baik
- **Caption**: Saya akan membuat caption otomatis dari informasi Anda

### Timeline/Sidebar

Skill akan secara otomatis membuat timeline yang mencakup:
- Tahun dan tanggal penting
- Milestone/pencapaian besar
- Perubahan lokasi
- Peristiwa keluarga penting

---

## Contoh Interaksi

### Pertanyaan dari Skill:
```
📖 BIOGRAFI WRITER - TAHAPAN 1: MASA KECIL

Mari mulai dari awal! Saya ingin mengenal masa kecil Anda.

❓ Pertanyaan 1: Kapan dan di mana Anda lahir?
Contoh: "Lahir 15 Januari 1975 di Jakarta, Rumah Sakit Pondok Indah"

Jawab: _________
```

### Jawaban dari User:
```
Lahir 15 Januari 1975 di Jakarta, tepatnya di Rumah Sakit Pondok Indah. Orang tua saya 
bernama Bapak Sutrisno dan Ibu Endang. Ayah bekerja di perusahaan minyak, ibu seorang guru.
```

### Output Chapter yang Dihasilkan:
```
BAB 1: MASA KECIL (1975-1987)

John Sutrisno dilahirkan pada fajar 15 Januari 1975 di Rumah Sakit Pondok Indah, Jakarta. 
Orang tuanya, Sutrisno dan Endang, menyambut kedatangannya dengan penuh kegembiraan. Ayahnya 
bekerja di industri minyak—sebuah pekerjaan yang akan membentuk karakteristik keluarga mereka 
yang selalu bergerak dan adaptif. Ibunya, seorang pendidik, membawa nilai-nilai pembelajaran 
dan kesabaran ke dalam rumah mereka.

Masa kecil John diwarnai oleh kehangatan keluarga yang solid meskipun mereka sering pindah 
mengikuti penugasan ayahnya...
```

## Kapan Gunakan Skill Ini

✓ Membuat memoir atau autobiografi pribadi  
✓ Menulis biografi profesional untuk profil perusahaan  
✓ Mendokumentasikan cerita hidup anggota keluarga  
✓ Membuat dokumen biografi untuk arsip keluarga atau sejarah  
✓ Mengubah catatan pribadi yang berantakan menjadi narasi polished  
✓ Membangun dokumen warisan (legacy document) dari kenangan yang tersebar  
✓ Persiapan ulang tahun atau perayaan khusus (dengan biografi yang elegan)  
✓ Arsip keluarga atau sejarah komunitas

---

## Fitur-Fitur Unggulan

### 📝 Guided Interview System
Pertanyaan terstruktur membimbing Anda melalui setiap tahapan kehidupan dengan natural. Tidak perlu menulis sendiri—cukup jawab pertanyaan!

### 🏗️ Struktur 6 Bab Default
1. **Masa Kecil** - Awal mula, keluarga, peristiwa formative
2. **Pendidikan** - Sekolah, prestasi, mentor berpengaruh
3. **Karir Awal** - Pekerjaan pertama, tantangan awal, pertumbuhan
4. **Pencapaian Utama** - Kesuksesan besar, penghargaan, dampak
5. **Kehidupan Keluarga** - Hubungan, keluarga, nilai-nilai personal
6. **Warisan/Legasi** - Kontribusi, pesan, kesan yang ditinggalkan

### 📸 Integrasi Foto
- Upload foto untuk setiap tahapan (optional)
- Foto ditempatkan secara otomatis di lokasi relevan
- Caption digenerate otomatis berdasarkan konteks

### 📑 Daftar Isi Otomatis
- Table of Contents yang dihasilkan secara otomatis
- Nomor halaman yang akurat
- Hyperlink yang dapat diklik (dalam PDF/digital)

### 📊 Timeline/Sidebar Visual
- Chronological timeline dari semua milestone
- Sidebar yang menampilkan tanggal dan event penting
- Membantu pembaca melacak perjalanan hidup

### 🎨 Formatting Profesional
- Font yang konsisten dan mudah dibaca
- Spacing yang tepat untuk publikasi
- Header dan footer
- Siap untuk printing atau distribusi digital

---

## Catatan Teknis

- Generate dokumen `.docx` yang kompatibel dengan Microsoft Word, Google Docs, dan software office lainnya
- Formatting profesional yang siap cetak
- Support penuh untuk images, text formatting, table of contents
- Proses otomatis mengubah jawaban menjadi narasi kohesif

## Next Steps

Untuk mulai membuat biografi, cukup katakan: **"Saya ingin membuat biografi menggunakan Biography Writer skill"** dan kami akan mulai interview interaktif untuk mengumpulkan semua informasi yang diperlukan!
