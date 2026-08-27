#!/usr/bin/env python3
"""
Biography Writer - Interactive Interview System
Guides users through structured questions for each life stage.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass

@dataclass
class Question:
    """Represents a single interview question."""
    id: str
    text: str
    category: str
    required: bool = True
    help_text: Optional[str] = None
    answer_type: str = "text"  # text, date, narrative, number

class InterviewSystem:
    """Manages the guided interview process."""
    
    def __init__(self, person_name: str):
        self.person_name = person_name
        self.responses = {}
        self.current_stage = 0
        self.questions = self._initialize_questions()
    
    def _initialize_questions(self) -> Dict[str, List[Question]]:
        """Initialize all interview questions for each life stage."""
        return {
            'masa_kecil': [
                Question(
                    id='birth_date',
                    text='Kapan dan di mana Anda dilahirkan?',
                    category='masa_kecil',
                    help_text='Contoh: "15 Januari 1975 di Jakarta, Rumah Sakit Pondok Indah"',
                    answer_type='date'
                ),
                Question(
                    id='parents',
                    text='Siapa nama orang tua Anda dan apa pekerjaan mereka?',
                    category='masa_kecil',
                    help_text='Sertakan nama ibu dan ayah, serta pekerjaan mereka'
                ),
                Question(
                    id='family_condition',
                    text='Bagaimana kondisi keluarga Anda pada masa kecil?',
                    category='masa_kecil',
                    answer_type='narrative',
                    help_text='Ceritakan tentang suasana keluarga, hubungan antar anggota keluarga, dan nilai-nilai yang diajarkan'
                ),
                Question(
                    id='childhood_events',
                    text='Apa peristiwa atau momen penting yang Anda ingat dari masa kecil?',
                    category='masa_kecil',
                    answer_type='narrative',
                    help_text='Ceritakan anekdot, pengalaman berkesan, atau pencapaian kecil yang berkesan'
                ),
                Question(
                    id='childhood_challenges',
                    text='Apa tantangan atau kesulitan yang Anda hadapi di masa kecil?',
                    category='masa_kecil',
                    answer_type='narrative',
                    required=False
                ),
                Question(
                    id='childhood_photo',
                    text='Apakah Anda memiliki foto dari masa kecil yang ingin ditampilkan?',
                    category='masa_kecil',
                    answer_type='text',
                    required=False,
                    help_text='Sebutkan path file foto (opsional)'
                ),
            ],
            'pendidikan': [
                Question(
                    id='schools_attended',
                    text='Sekolah mana saja yang Anda hadiri? (SD, SMP, SMA, Universitas)',
                    category='pendidikan',
                    answer_type='narrative',
                    help_text='Sertakan nama sekolah dan tahun masuk/lulus'
                ),
                Question(
                    id='academic_achievements',
                    text='Apa prestasi akademik yang Anda raih?',
                    category='pendidikan',
                    answer_type='narrative',
                    help_text='Nilai terbaik, peringkat, beasiswa, penghargaan akademik, dll'
                ),
                Question(
                    id='influential_teachers',
                    text='Apakah ada guru atau mentor yang sangat berpengaruh pada Anda?',
                    category='pendidikan',
                    answer_type='narrative',
                    required=False,
                    help_text='Ceritakan tentang guru/mentor itu dan bagaimana mereka mempengaruhi Anda'
                ),
                Question(
                    id='memorable_school_experience',
                    text='Pengalaman apa di sekolah yang paling berkesan atau mengubah Anda?',
                    category='pendidikan',
                    answer_type='narrative',
                    help_text='Bisa berupa prestasi, kejadian lucu, pembelajaran penting, atau momen persahabatan'
                ),
                Question(
                    id='school_photos',
                    text='Apakah ada foto dari masa sekolah yang ingin ditampilkan?',
                    category='pendidikan',
                    answer_type='text',
                    required=False
                ),
            ],
            'karir_awal': [
                Question(
                    id='first_job',
                    text='Apa pekerjaan pertama Anda dan kapan Anda memulainya?',
                    category='karir_awal',
                    answer_type='text',
                    help_text='Contoh: "Junior Developer di PT Tech Indonesia, tahun 2000"'
                ),
                Question(
                    id='job_motivation',
                    text='Apa yang mendorong Anda memilih pekerjaan/industri tersebut?',
                    category='karir_awal',
                    answer_type='narrative'
                ),
                Question(
                    id='early_challenges',
                    text='Tantangan apa yang Anda hadapi di awal karir?',
                    category='karir_awal',
                    answer_type='narrative',
                    help_text='Kesulitan adaptasi, kurva pembelajaran yang curam, konflik, dll'
                ),
                Question(
                    id='early_achievements',
                    text='Apa pencapaian atau milestone pertama yang berarti dalam karir Anda?',
                    category='karir_awal',
                    answer_type='narrative',
                    help_text='Proyek sukses pertama, promosi, penghargaan, atau kepercayaan dari atasan'
                ),
                Question(
                    id='skill_development',
                    text='Keterampilan apa yang Anda kembangkan di fase awal karir ini?',
                    category='karir_awal',
                    answer_type='narrative',
                    required=False
                ),
            ],
            'pencapaian_utama': [
                Question(
                    id='greatest_achievement',
                    text='Apa pencapaian terbesar Anda dalam hidup?',
                    category='pencapaian_utama',
                    answer_type='narrative',
                    help_text='Bisa berupa kesuksesan profesional, proyek berdampak, atau pencapaian personal'
                ),
                Question(
                    id='awards_recognition',
                    text='Penghargaan atau pengakuan apa yang Anda terima?',
                    category='pencapaian_utama',
                    answer_type='narrative',
                    required=False,
                    help_text='Penghargaan profesional, sertifikasi, gelar kehormatan, dll'
                ),
                Question(
                    id='major_projects',
                    text='Proyek atau inisiatif penting apa yang Anda pimpin atau terlibat?',
                    category='pencapaian_utama',
                    answer_type='narrative',
                    help_text='Jelaskan tujuan, tantangan, dan hasil dari proyek tersebut'
                ),
                Question(
                    id='impact_created',
                    text='Dampak apa yang Anda ciptakan melalui pencapaian ini?',
                    category='pencapaian_utama',
                    answer_type='narrative',
                    help_text='Dampak pada organisasi, industri, masyarakat, atau individu'
                ),
                Question(
                    id='achievement_photo',
                    text='Apakah ada foto atau dokumentasi dari pencapaian Anda yang ingin ditampilkan?',
                    category='pencapaian_utama',
                    answer_type='text',
                    required=False
                ),
            ],
            'kehidupan_keluarga': [
                Question(
                    id='marriage_partnership',
                    text='Apakah Anda menikah atau memiliki hubungan jangka panjang yang penting?',
                    category='kehidupan_keluarga',
                    answer_type='narrative',
                    required=False,
                    help_text='Ceritakan tentang pasangan Anda dan bagaimana Anda bertemu'
                ),
                Question(
                    id='children',
                    text='Apakah Anda memiliki anak? Ceritakan tentang mereka.',
                    category='kehidupan_keluarga',
                    answer_type='narrative',
                    required=False,
                    help_text='Nama, tahun lahir, dan apa yang membanggakan dari mereka'
                ),
                Question(
                    id='family_values',
                    text='Nilai-nilai keluarga apa yang penting bagi Anda?',
                    category='kehidupan_keluarga',
                    answer_type='narrative',
                    help_text='Nilai moral, tradisi, prinsip yang Anda pegang teguh'
                ),
                Question(
                    id='work_life_balance',
                    text='Bagaimana Anda menyeimbangkan karir dan kehidupan keluarga?',
                    category='kehidupan_keluarga',
                    answer_type='narrative',
                    required=False
                ),
                Question(
                    id='memorable_family_moments',
                    text='Momen keluarga apa yang paling Anda hargai atau ingat?',
                    category='kehidupan_keluarga',
                    answer_type='narrative',
                    required=False,
                    help_text='Liburan spesial, tradisi keluarga, pencapaian bersama'
                ),
                Question(
                    id='family_photo',
                    text='Apakah ada foto keluarga yang ingin ditampilkan?',
                    category='kehidupan_keluarga',
                    answer_type='text',
                    required=False
                ),
            ],
            'warisan': [
                Question(
                    id='biggest_contribution',
                    text='Apa kontribusi terbesar Anda bagi masyarakat atau industri Anda?',
                    category='warisan',
                    answer_type='narrative'
                ),
                Question(
                    id='values_to_leave',
                    text='Nilai atau pesan apa yang ingin Anda tinggalkan untuk generasi mendatang?',
                    category='warisan',
                    answer_type='narrative'
                ),
                Question(
                    id='how_remembered',
                    text='Bagaimana Anda ingin diingat oleh orang-orang?',
                    category='warisan',
                    answer_type='narrative'
                ),
                Question(
                    id='future_plans',
                    text='Apa rencana atau impian Anda untuk masa depan?',
                    category='warisan',
                    answer_type='narrative',
                    required=False
                ),
                Question(
                    id='wisdom_learned',
                    text='Apa pelajaran hidup paling penting yang Anda peroleh?',
                    category='warisan',
                    answer_type='narrative'
                ),
            ]
        }
    
    def get_stage_questions(self, stage: str) -> List[Question]:
        """Get all questions for a specific life stage."""
        return self.questions.get(stage, [])
    
    def save_answer(self, question_id: str, answer: str, stage: str) -> None:
        """Save an answer to a specific question."""
        if stage not in self.responses:
            self.responses[stage] = {}
        self.responses[stage][question_id] = answer
    
    def get_answers_by_stage(self, stage: str) -> Dict[str, str]:
        """Get all answers for a specific life stage."""
        return self.responses.get(stage, {})
    
    def generate_stage_summary(self, stage: str) -> str:
        """Generate a summary of all answers for a stage."""
        answers = self.get_answers_by_stage(stage)
        questions = self.get_stage_questions(stage)
        
        summary = []
        for q in questions:
            if q.id in answers:
                summary.append(f"Q: {q.text}\nA: {answers[q.id]}\n")
        
        return "\n".join(summary)
    
    def is_stage_complete(self, stage: str) -> bool:
        """Check if all required questions for a stage have been answered."""
        answers = self.get_answers_by_stage(stage)
        questions = self.get_stage_questions(stage)
        
        for q in questions:
            if q.required and q.id not in answers:
                return False
        return True


def main():
    """Example usage of InterviewSystem."""
    # Create interview system
    interview = InterviewSystem("John Doe")
    
    # Get questions for first stage
    masa_kecil_questions = interview.get_stage_questions('masa_kecil')
    
    print("=== BIOGRAPHY WRITER - GUIDED INTERVIEW ===\n")
    print(f"Welcome! Let's create a biography for {interview.person_name}\n")
    
    print("TAHAPAN 1: MASA KECIL\n")
    
    for question in masa_kecil_questions:
        print(f"❓ {question.text}")
        if question.help_text:
            print(f"   💡 {question.help_text}")
        
        # Simulated user input
        answer = input("\n📝 Jawab: ")
        
        if question.required and not answer.strip():
            print("   ⚠️  Pertanyaan ini wajib dijawab")
            continue
        
        interview.save_answer(question.id, answer, 'masa_kecil')
        print("   ✓ Jawaban tersimpan\n")
    
    # Show summary
    print("\n=== RINGKASAN MASA KECIL ===\n")
    print(interview.generate_stage_summary('masa_kecil'))


if __name__ == '__main__':
    main()
