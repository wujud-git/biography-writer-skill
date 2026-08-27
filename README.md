# Biography Writer Skill

Transform biographical data into beautifully structured narrative books organized by life stages.

## 📁 Struktur Folder

```
biography-writer/
├── SKILL.md                          # Dokumentasi skill utama
├── README.md                         # File ini
├── test_cases.json                   # Test cases untuk evaluasi skill
├── scripts/
│   ├── biography_generator.py        # Script untuk generate dokumen Word
│   └── interview_system.py           # Script untuk guided interview
└── references/
    └── (future: referensi tambahan)
```

## 🚀 Quick Start

### Cara Kerja Skill

1. **User memberi tahu**: "Saya ingin membuat biografi"
2. **Skill melakukan interview**: Mengajukan pertanyaan terstruktur untuk setiap tahapan kehidupan
3. **User menjawab pertanyaan**: Memberikan informasi tentang masa kecil, pendidikan, karir, dll
4. **Skill menghasilkan dokumen**: Dokumen Word (.docx) dengan 6 bab yang kohesif

### Tahapan Kehidupan (Life Stages)

Skill otomatis mengorganisir informasi ke dalam 6 bab:

1. **MASA KECIL** (Early Life)
   - Tempat lahir, orang tua, kondisi keluarga
   - Peristiwa penting dan tantangan

2. **PENDIDIKAN** (Education)
   - Sekolah yang dihadiri, prestasi akademik
   - Guru/mentor berpengaruh, pengalaman berkesan

3. **KARIR AWAL** (Early Career)
   - Pekerjaan pertama, motivasi karir
   - Tantangan awal, pencapaian pertama

4. **PENCAPAIAN UTAMA** (Major Achievements)
   - Pencapaian terbesar, penghargaan
   - Proyek penting, dampak yang dihasilkan

5. **KEHIDUPAN KELUARGA** (Family Life)
   - Pernikahan/hubungan, anak-anak
   - Nilai keluarga, work-life balance

6. **WARISAN/LEGASI** (Legacy)
   - Kontribusi terbesar, nilai yang ditinggalkan
   - Bagaimana ingin diingat, rencana masa depan

## 📝 Fitur Utama

✅ **Guided Interview** - Pertanyaan interaktif untuk setiap tahapan  
✅ **Flexible Input** - Terima jawaban dalam bentuk list atau narasi panjang  
✅ **Narrative Generation** - Konversi jawaban menjadi paragraf semi-formal (3-5 per bab)  
✅ **Photo Integration** - Masukkan foto dengan caption otomatis  
✅ **Auto Table of Contents** - TOC yang di-generate otomatis  
✅ **Timeline/Sidebar** - Visualisasi chronological dari milestone hidup  
✅ **Professional Formatting** - Document siap cetak  

## 🧪 Testing

### Menjalankan Test Cases

```bash
# Test 1: Basic biography generation
python scripts/biography_generator.py

# Test dengan interview system
python scripts/interview_system.py
```

### Test Cases yang Tersedia

Lihat `test_cases.json` untuk 5 test scenario:

1. **Basic Biography Generation** - Full biography dengan data lengkap
2. **Minimal Data** - Biography dengan data yang terbatas
3. **Detailed Narrative** - Biography dengan narasi yang panjang
4. **Multiple Photos** - Test integrasi multiple photos
5. **Timeline Completeness** - Test timeline generation dengan 8 events

## 🔧 Implementasi Technical

### Dependencies

- `python-docx` - Untuk generate dokumen Word
- `Pillow` - Untuk image handling/resizing
- Python 3.8+

### Komponen Utama

#### `BiographyGenerator` (biography_generator.py)

```python
bg = BiographyGenerator("John Doe")
bg.add_chapter_data('masa_kecil', {...})
bg.add_photo('masa_kecil', '/path/to/photo.jpg', 'Caption')
bg.add_timeline_event(1975, 'Lahir', month=1)
bg.save('output.docx')
```

#### `InterviewSystem` (interview_system.py)

```python
interview = InterviewSystem("John Doe")
questions = interview.get_stage_questions('masa_kecil')
interview.save_answer('birth_date', 'answer', 'masa_kecil')
interview.is_stage_complete('masa_kecil')
```

## 📋 Workflow Lengkap

```
User: "Saya ingin membuat biografi"
        ↓
Claude: "Mari kita mulai! Siapa nama Anda?"
        ↓
User: "John Doe"
        ↓
Claude: "Bagus! Mari kita mulai tahapan 1: MASA KECIL"
        ↓
[Interview System] ← Mengajukan 5-6 pertanyaan per tahapan
        ↓
[User menjawab pertanyaan] ← 6 tahapan × 5-6 pertanyaan = ~36 pertanyaan total
        ↓
[Skill mengumpulkan semua jawaban]
        ↓
[API Claude] → Generate narasi 3-5 paragraf per bab
        ↓
[Biography Generator] → Create Word document dengan:
  - Title page
  - Table of Contents
  - 6 bab dengan narasi
  - Photos (jika ada)
  - Timeline (jika ada)
  - Professional formatting
        ↓
Output: biography_john_doe.docx
```

## 🎯 Evaluation Criteria

### Untuk Dievaluasi

1. **Document Structure** - Title page, TOC, chapters, timeline
2. **Narrative Quality** - Paragraph flow, tone, coherence
3. **Photo Integration** - Placement, captions, formatting
4. **Technical** - File format, compatibility, file size

Lihat `test_cases.json` untuk detail criteria.

## 📸 Contoh Output

Dokumen yang dihasilkan akan terlihat seperti:

```
═══════════════════════════════════════
        JOHN DOE
        Biografi Lengkap
    Digenerate: 20 Agustus 2026
═══════════════════════════════════════

DAFTAR ISI
1. MASA KECIL
2. PENDIDIKAN
3. KARIR AWAL
4. PENCAPAIAN UTAMA
5. KEHIDUPAN KELUARGA
6. WARISAN DAN LEGASI
7. TIMELINE KEHIDUPAN

═══════════════════════════════════════

BAB 1: MASA KECIL

John Doe dilahirkan pada 15 Januari 1975 di Jakarta...
[3-5 paragraf dengan foto jika ada]

[Repeat untuk 5 bab lainnya]

═══════════════════════════════════════

TIMELINE KEHIDUPAN
• Januari 1975 - Lahir di Jakarta
• 1981 - Masuk SD Negeri 1
• 1987 - Lulus SD, masuk SMP
• ... dst
```

## 🔄 Next Steps

1. ✅ Draft SKILL.md - Selesai
2. ✅ Script biography_generator.py - Selesai
3. ✅ Script interview_system.py - Selesai
4. ✅ Test cases - Selesai
5. ⏳ **Run test cases** - Berikutnya
6. ⏳ Iterasi berdasarkan hasil testing
7. ⏳ Optimize description untuk triggering
8. ⏳ Package skill

## 📞 Support

Untuk questions atau issues tentang skill ini, silakan tanyakan pada Claude dengan reference ke skill ini.

---

**Status**: Draft siap untuk testing  
**Last Updated**: Agustus 2026  
**Version**: 1.0
