# Biography Writer Skill - GitHub Setup Guide

**Goal**: Upload Biography Writer Skill ke GitHub Repository

---

## Step 1: Clone Repository Anda

```bash
# Buka terminal/command prompt
cd ~/Documents  # atau folder mana saja yang Anda inginkan

# Clone repository yang baru Anda buat
git clone https://github.com/[USERNAME]/biography-writer-skill.git

# Masuk ke folder
cd biography-writer-skill
```

---

## Step 2: Copy Semua Files Berikut ke Repository

Berikut adalah **struktur folder yang harus Anda buat**:

```
biography-writer-skill/
├── README.md                          # Copy dari dokumentasi kami
├── LICENSE                            # MIT License
├── SKILL.md                          # Copy skill documentation
├── .gitignore                        # Python .gitignore
│
├── scripts/
│   ├── __init__.py                   # Empty file
│   ├── biography_generator.py        # Core engine
│   └── interview_system.py           # Interview system
│
├── docs/
│   ├── EVALUATION_REPORT.md
│   ├── PRODUCTION_APPROVAL.md
│   ├── LAUNCH_MATERIALS.md
│   ├── SUPPORT_DOCUMENTATION.md
│   ├── DISTRIBUTION_MANIFEST.md
│   └── DEPLOYMENT_COMPLETE.md
│
├── tests/
│   ├── test_cases.json
│   ├── run_test_case_1.py
│   └── run_all_tests.py
│
├── samples/
│   ├── biography_siti_nurhaliza.docx
│   ├── biography_ahmad_rahman.docx
│   ├── biography_dr_bambang_sutrisno.docx
│   ├── biography_ria_irawan.docx
│   ├── biography_ir_djoko_hartono.docx
│   └── biography_john_doe.docx
│
└── requirements.txt                   # Dependencies list
```

---

## Step 3: Buat File requirements.txt

Buat file bernama `requirements.txt` di root folder dengan konten:

```
python-docx>=0.8.11
Pillow>=8.0.0
```

---

## Step 4: Buat File .gitignore

Jika belum ada, buat file `.gitignore` dengan:

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Generated files
*.docx
biography_*.docx
.pytest_cache/
```

---

## Step 5: Git Add, Commit, Push

```bash
# Tambahkan semua files
git add .

# Commit
git commit -m "Initial commit: Biography Writer Skill v1.0 - Production Ready"

# Push ke GitHub
git push origin main
```

---

## Step 6: Verify di GitHub

Buka https://github.com/[USERNAME]/biography-writer-skill

Anda seharusnya melihat:
✅ Semua files ter-upload
✅ README.md tampil di halaman utama
✅ Folder structure terlihat rapi
✅ Documentation tersedia

---

## Step 7: Optional - Add Topics

Di GitHub repository settings, add topics:
- `biography`
- `skill`
- `claude`
- `python`
- `word-document`
- `automation`

Ini membantu orang menemukan skill Anda!

---

## Step 8: Optional - Create Release

Untuk menandai versi, buat release:

```bash
# Tag version
git tag -a v1.0 -m "Biography Writer Skill v1.0 - First Release"
git push origin v1.0
```

Kemudian di GitHub, buat Release dari tag ini dengan release notes.

---

## Troubleshooting

### Error: "fatal: not a git repository"
```bash
# Pastikan Anda di dalam folder repository
pwd  # Cek lokasi
cd biography-writer-skill  # Masuk ke folder yang benar
```

### Error: "authentication failed"
```bash
# Setup GitHub credentials
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Atau gunakan token (lebih aman)
# Lihat: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
```

### Files tidak ter-upload
```bash
# Cek status
git status

# Tambahkan specific file
git add scripts/biography_generator.py
git commit -m "Add core script"
git push
```

---

## SELESAI! ✅

Repository Anda sekarang aktif di GitHub dan bisa diakses oleh orang lain!

**Next**: Ke TAHAP 2 - Gunakan Langsung di Claude
