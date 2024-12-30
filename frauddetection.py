from textblob import TextBlob
import re

class FakeNewsDetector:
    def __init__(self):
        # Dictionary kata kunci yang sering muncul di berita palsu
        self.keyword_dict = {
            'clickbait': [r'\bviral\b', r'\bmengejutkan\b', r'\btidak disangka\b', r'\bmasih ingat\b'],
            'emotional': ['mencengangkan', 'menggemparkan', 'heboh', 'mengharukan', 'panik', 'waspada'],
            'urgency': [r'\bsebarkan\b', r'\bshare\b', r'\bbagikan segera\b', r'\bbreaking news\b', 
                        r'\burgent\b', r'\bsegera\b', r'\bsebelum terlambat\b', r'\bperlu diketahui\b'],
            'hoax_keywords': [r'\btidak benar\b', r'\bpalsu\b', r'\bhoax\b', r'\bkonspirasi\b', r'\bteori\b', r'\b3 periode\b'],
            'phising' : ['klik', 'daftar', 'masukkan', 'login', 'password', 'username', 'akun', 
                        'verifikasi', 'email', 'link', 'website', 'informasi', 'data', 'uang', 
                        'gratis', 'voucher', 'promo', 'hadiah', 'pemenang', 'menang', 'kemenangan', 'berhadiah', 'beruntung']
        }

        # Logika berbasis poin
        self.logic_rules = [
            ('if_contradictory', -0.2),
            ('has_source', 0.3),
            ('emotional_language', -0.1),
            ('clickbait', -0.1),
            ('urgency', -0.1),
            ('hoax_indicators', -0.2),
            ('phising', -0.1)
        ]

    def analyze_text(self, text, hoax, urgency, emotional, clickbait, sentiment_negatif, kontradiksi, phising):
        # Analisis utama teks
        score = 0.5  # Score awal 0.5 dianggap netral

        # Memeriksa kontradiksi dalam teks
        sentences = text.split('.')
        contradictions = 0

        for i in range(len(sentences)):
            for j in range(i + 1, len(sentences)):
                words1 = set(sentences[i].lower().split())
                words2 = set(sentences[j].lower().split())
                if len(words1 & words2) > 0 and len(words1.symmetric_difference(words2)) > 5:
                    contradictions += 1

        if contradictions > 0:
            score += self.logic_rules[0][1]
            kontradiksi = True

        # Memeriksa kutipan sumber
        source_patterns = [
            r'menurut\s+([^,\.]+)',
            r'berdasarkan\s+([^,\.]+)',
            r'dikutip\s+dari\s+([^,\.]+)',
            r'sumber\s+([^,\.]+)'
        ]

        if any(re.search(pattern, text.lower()) for pattern in source_patterns):
            score += self.logic_rules[1][1]

        # Cek penggunaan bahasa emosional
        emotional_count = sum(word in self.keyword_dict['emotional'] for word in text.lower().split())
        if emotional_count > 0:  # Kurang dari 2 pun cukup untuk deteksi
            score += self.logic_rules[2][1]
            emotional = True

        # Cek clickbait
        clickbait_count = sum(bool(re.search(pattern, text.lower())) for pattern in self.keyword_dict['clickbait'])
        if clickbait_count > 0:
            score += self.logic_rules[3][1]
            clickbait = True

        # Cek urgensi
        urgency_count = sum(bool(re.search(pattern, text.lower())) for pattern in self.keyword_dict['urgency']) 
        if urgency_count > 0:
            score += self.logic_rules[4][1]
            urgency = True

        # Cek indikasi hoax
        hoax_count = sum(bool(re.search(pattern, text.lower())) for pattern in self.keyword_dict['hoax_keywords'])
        if hoax_count > 0:
            score += self.logic_rules[5][1]
            hoax = True
        
        # Cek indikasi phising
        phising_count = sum(word in self.keyword_dict['phising'] for word in text.lower().split())
        if phising_count > 0:
            score += self.logic_rules[6][1]
            phising = True

        # Analisis sentimen tambahan
        sentiment = TextBlob(text).sentiment.polarity
        if sentiment < -0.5:
            sentiment_negatif = True

        return max(0, min(1, score)), hoax, urgency, emotional, clickbait, sentiment_negatif, kontradiksi, phising
        # Normalize score between 0 and 1

    def classify(self, text):
        # Inisialisasi logika proposisi berbasis boolean
        hoax = False 
        urgency = False
        emotional = False
        clickbait = False
        kontradiksi = False
        sentiment_negatif = False
        phising = False

        detected_features = []

        score, hoax, urgency, emotional, clickbait, kontradiksi, sentiment_negatif, phising = self.analyze_text(text, hoax, urgency, emotional, clickbait, kontradiksi, sentiment_negatif, phising)

    # Contoh implementasi dengan operasi AND proposisi
        # if hoax and urgency and emotional and clickbait: #kondisional dengan operasi AND 
        #     detected_features.append("indikator hoax, urgency, bahasa emosional, clickbait")
        # elif hoax and urgency and emotional: #kondisional dengan operasi AND
        #     detected_features.append("indikator hoax, urgency, bahasa emosional")

    # Karena terlalu banyak dan tidak efektif, maka diaplikasikan dengan operasi percabangan biasa

        if hoax:
            detected_features.append("indikator hoax")
        if clickbait:
            detected_features.append("clickbait")
        if urgency:
            detected_features.append("urgency")
        if emotional:
            detected_features.append("bahasa emosional")
        if sentiment_negatif < -0.5:
            detected_features.append("sentimen negatif")
        if phising:
            detected_features.append("indikator phising")

        if detected_features:
            feature_message = ", ".join(detected_features)  
        else: 
            feature_message = "tidak ada karakteristik mencurigakan"

        if score < 0.4:
            return f"Kemungkinan Berita Palsu dengan fitur: {feature_message}", score
        elif score > 0.6:
            return f"Kemungkinan Berita Valid dengan fitur: {feature_message}", score
        else:
            return f"Perlu Verifikasi Lebih Lanjut dengan fitur: {feature_message}", score
