import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

# Register Arial with full Turkish character support
font_path = "C:/Windows/Fonts/arial.ttf"
font_bold_path = "C:/Windows/Fonts/arialbd.ttf"
pdfmetrics.registerFont(TTFont("Arial", font_path))
pdfmetrics.registerFont(TTFont("Arial-Bold", font_bold_path))

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Arial", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        
        # Header (pages 2+)
        if self._pageNumber > 1:
            self.drawString(36, 810, "AI Sales Director (/sales-manager) — E-Ticaret Kazanan Ürün & Reklam Stratejisi")
            self.setStrokeColor(colors.HexColor("#E2E8F0"))
            self.setLineWidth(0.5)
            self.line(36, 804, 559, 804)

        # Footer (all pages)
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(36, 40, 559, 40)
        
        self.drawString(36, 28, "GitHub: https://github.com/EthYusuf/ai-sales-director  |  Model Context Protocol (MCP)")
        page_str = f"Sayfa {self._pageNumber} / {page_count}"
        self.drawRightString(559, 28, page_str)
        self.restoreState()

pdf_filename = "AI_Sales_Director_Master_Guide.pdf"
doc = SimpleDocTemplate(
    pdf_filename,
    pagesize=A4,
    leftMargin=36,
    rightMargin=36,
    topMargin=46,
    bottomMargin=50
)

# Colors
primary_navy = colors.HexColor("#0F172A")
royal_blue = colors.HexColor("#1E40AF")
accent_blue = colors.HexColor("#2563EB")
sky_blue = colors.HexColor("#0284C7")
emerald_green = colors.HexColor("#059669")
bg_light = colors.HexColor("#F8FAFC")
bg_highlight = colors.HexColor("#EFF6FF")
border_gray = colors.HexColor("#CBD5E1")
text_dark = colors.HexColor("#1E293B")
text_muted = colors.HexColor("#475569")
danger_red = colors.HexColor("#DC2626")

# Styles
cover_title_style = ParagraphStyle(
    "CoverTitle",
    fontName="Arial-Bold",
    fontSize=22,
    leading=26,
    textColor=colors.white,
    alignment=1
)

cover_subtitle_style = ParagraphStyle(
    "CoverSub",
    fontName="Arial",
    fontSize=11,
    leading=15,
    textColor=colors.HexColor("#BFDBFE"),
    alignment=1
)

h1_style = ParagraphStyle(
    "SectionH1",
    fontName="Arial-Bold",
    fontSize=13,
    leading=16,
    textColor=royal_blue,
    spaceBefore=8,
    spaceAfter=4
)

h2_style = ParagraphStyle(
    "SectionH2",
    fontName="Arial-Bold",
    fontSize=10.5,
    leading=14,
    textColor=primary_navy,
    spaceBefore=6,
    spaceAfter=3
)

body_style = ParagraphStyle(
    "BodyTextCustom",
    fontName="Arial",
    fontSize=8.5,
    leading=12,
    textColor=text_dark
)

callout_style = ParagraphStyle(
    "CalloutText",
    fontName="Arial",
    fontSize=8.5,
    leading=12,
    textColor=colors.HexColor("#1E3A8A")
)

tbl_hdr_style = ParagraphStyle(
    "TableHdr",
    fontName="Arial-Bold",
    fontSize=8.5,
    leading=11,
    textColor=colors.white
)

tbl_cell_style = ParagraphStyle(
    "TableCell",
    fontName="Arial",
    fontSize=8,
    leading=10.5,
    textColor=text_dark
)

tbl_cell_bold = ParagraphStyle(
    "TableCellBold",
    fontName="Arial-Bold",
    fontSize=8,
    leading=10.5,
    textColor=primary_navy
)

story = []

# ==========================================
# PAGE 1: COVER & EXECUTIVE SUMMARY
# ==========================================
cover_table_data = [
    [Paragraph("AI SALES DIRECTOR (/sales-manager)", cover_title_style)],
    [Spacer(1, 4)],
    [Paragraph("E-TİCARET KAZANAN ÜRÜN KEŞFİ, KÜRESEL PAZAR ANALİZİ & VİRAL REKLAM STRATEJİSİ", cover_subtitle_style)],
    [Paragraph("Model Context Protocol (MCP) & Evrensel Yapay Zeka Beceri El Kitabı", cover_subtitle_style)]
]
cover_table = Table(cover_table_data, colWidths=[523])
cover_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), primary_navy),
    ("TOPPADDING", (0, 0), (-1, -1), 16),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 16),
    ("LEFTPADDING", (0, 0), (-1, -1), 14),
    ("RIGHTPADDING", (0, 0), (-1, -1), 14),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
]))
story.append(cover_table)
story.append(Spacer(1, 12))

story.append(Paragraph("1. YÖNETİCİ ÖZETİ: E-Ticarette Ürün Seçimi Neden Hayati Önemdedir?", h1_style))
story.append(Paragraph(
    "Global e-ticaret ve dropshipping sektöründe başarısız olan girişimcilerin <b>%87'si</b> teknik yetersizlikten değil, "
    "<b>yanlış ürün seçimi</b> ve <b>hatalı pazar hedeflemesi</b> yüzünden sermayesini kaybetmektedir. "
    "Çoğu girişimci ürün seçerken sübjektif hislerine güvenir ve reklam bütçesini doğrudan harcamaya başlar. "
    "Oysa e-ticaret bir matematik oyunudur: Bir ürünün satabilmesi için doğrulanmış bir acıyı çözmesi, video akışında parmak kaydırmayı durdurması (Scroll-stopper), "
    "minimum 3x kâr çarpanına sahip olması ve doğru coğrafyada doğru kitleye sunulması şarttır.",
    body_style
))
story.append(Spacer(1, 6))

story.append(Paragraph("E-Ticaret Girişimcilerinin Düştüğü 5 Ölümcül Hata:", h2_style))
mistakes_data = [
    [Paragraph("Hata", tbl_hdr_style), Paragraph("Neden Tehlikelidir?", tbl_hdr_style), Paragraph("AI Sales Director Çözümü", tbl_hdr_style)],
    [Paragraph("1. Düşük Marjlı Ürün Satmak", tbl_cell_bold), Paragraph("Ürünü $10'a alıp $18'e satmaya çalışmak; reklam maliyetleri (CAC) yükseldiğinde her siparişte zarar ettirir.", tbl_cell_style), Paragraph("3x Marj Kuralı ve Birim Maliyet (Unit Economics) denetimiyle minimum %65-%75 brüt marj şartı koşar.", tbl_cell_style)],
    [Paragraph("2. 'Vay Canına' Etkisi Olmayan Sıradan Ürün", tbl_cell_bold), Paragraph("Yerel bakkalda, süpermarkette veya yerel AVM'de kolayca bulunabilen ürünler dürtüsel internet alımına uygun değildir.", tbl_cell_style), Paragraph("Perakende Kıtlığı (Scarcity) ve İlk 3 Saniye Görsel Çekicilik puanlaması uygular.", tbl_cell_style)],
    [Paragraph("3. Ağır / Kırılabilir Ürün Seçimi", tbl_cell_bold), Paragraph("Cam, sıvı veya 1 kg üzeri ürünler yüksek kargo navlunu, gümrük hasarı ve %15+ iade oranı doğurur.", tbl_cell_style), Paragraph("Kargo Feasibility filtresiyle 500 gr altı, kırılmaz ve risksiz ürünleri önceliklendirir.", tbl_cell_style)],
    [Paragraph("4. Yanlış Ülkede Reklam Basmak", tbl_cell_bold), Paragraph("Gümrük engeli, düşük kredi kartı penetrasyonu veya yüksek kapıda ödeme iadesi olan ülkelere bütçe akıtmak.", tbl_cell_style), Paragraph("Tier 1 (ABD, İngiltere, Avustralya) ve Körfez (GCC) analiziyle hazır alıcı pazarları hedefler.", tbl_cell_style)],
    [Paragraph("5. Yanlış Reklam Platformu", tbl_cell_bold), Paragraph("Görsel gadget'ları Google Arama'da veya arama hacimli acil ihtiyaçları salt TikTok'ta zorlamak.", tbl_cell_style), Paragraph("Ürün doğasına göre TikTok vs Meta vs Google Shopping ayrımını net formüllerle yapar.", tbl_cell_style)]
]
mistakes_table = Table(mistakes_data, colWidths=[115, 204, 204])
mistakes_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), royal_blue),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, bg_light]),
    ("GRID", (0, 0), (-1, -1), 0.5, border_gray),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
]))
story.append(mistakes_table)
story.append(Spacer(1, 8))

callout_box_data = [[Paragraph(
    "💡 <b>AI Sales Director (/sales-manager) Sistemi</b>, bu 5 kritik ölümcül hatayı reklam paneline 1 dolar dahi yüklemeden önce "
    "algoritmik olarak tespit eder ve ürününüzü A'dan Z'ye denetleyerek net bir yol haritası sunar.",
    callout_style
)]]
callout_table = Table(callout_box_data, colWidths=[523])
callout_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), bg_highlight),
    ("BOX", (0, 0), (-1, -1), 1, royal_blue),
    ("PADDING", (0, 0), (-1, -1), 8),
]))
story.append(callout_table)

# ==========================================
# PAGE 2: 7 PILLARS & EVALUATION MATRIX
# ==========================================
story.append(PageBreak())

story.append(Paragraph("2. KAZANAN ÜRÜNÜN 7 ALTIN KURALI (THE 7 PILLARS)", h1_style))
story.append(Paragraph(
    "Bir e-ticaret ürününün 'Kazanan Ürün' (Winning Product) statüsüne erişebilmesi için aşağıdaki 7 sütun üzerinden incelenmesi gerekir. "
    "Sistem her bir kriteri analiz ederek 0 ile 100 arasında kurumsal bir <b>Kazanan Ürün Skoru</b> üretir:",
    body_style
))
story.append(Spacer(1, 6))

seven_pillars_data = [
    [Paragraph("Sütun / Kriter", tbl_hdr_style), Paragraph("Detaylı Açıklama & Analiz Metodu", tbl_hdr_style), Paragraph("Kritik Eşik", tbl_hdr_style)],
    [Paragraph("1. Acı / Problem Çözme", tbl_cell_bold), Paragraph("İnsanların fiziksel acısını dindiren (bel fıtığı yastığı), zaman kazandıran (sebze doğrayıcı) veya para tasarrufu sağlayan ürünler en hızlı dürtüsel satıştır.", tbl_cell_style), Paragraph("Puan: 9/10+", tbl_cell_bold)],
    [Paragraph("2. 'Vay Canına' Faktörü", tbl_cell_bold), Paragraph("TikTok veya Reels akışında ilk 3 saniyede izleyiciyi durduran, merak uyandıran veya tatmin edici (satisfying) görsel demonstrasyon gücü.", tbl_cell_style), Paragraph("Puan: 8/10+", tbl_cell_bold)],
    [Paragraph("3. 3x Fiyat Çarpanı", tbl_cell_bold), Paragraph("Tedarik + Kargo maliyeti örneğin $10 ise satış fiyatı en az $30-$35 olmalıdır. Reklam platformlarında kâra geçmek için brüt marj %70 civarında olmalıdır.", tbl_cell_style), Paragraph("Min. 3x Çarpan", tbl_cell_bold)],
    [Paragraph("4. Perakende Kıtlığı", tbl_cell_bold), Paragraph("Tüketici bu ürünü en yakın süpermarketten veya mahalle mağazasından hemen satın alamamalı; internetten siparişi tek alternatif olmalıdır.", tbl_cell_style), Paragraph("Özgün / Yenilikçi", tbl_cell_bold)],
    [Paragraph("5. Kargo & Lojistik", tbl_cell_bold), Paragraph("500 gram altı, kutulanması kolay, kırılgan cam veya tehlikeli batarya regülasyonlarına tabi olmayan hafif ürünler tercih edilmelidir.", tbl_cell_style), Paragraph("İade < %3", tbl_cell_bold)],
    [Paragraph("6. İçerik & UGC Uygunluğu", tbl_cell_bold), Paragraph("İçerik üreticilerinin (UGC Creators) ürünü kameraya karşı kolayca test edip Öncesi/Sonrası (Before & After) farkını gösterebilmesi.", tbl_cell_style), Paragraph("UGC Dostu", tbl_cell_bold)],
    [Paragraph("7. Pazar Büyüklüğü", tbl_cell_bold), Paragraph("Sadece 5.000 kişilik niş bir hobi değil; milyonlarca insana (anneler, sporcular, araç sahipleri, öğrenciler) hitap eden geniş ölçeklenme hacmi.", tbl_cell_style), Paragraph("Geniş Kitle", tbl_cell_bold)]
]
seven_pillars_table = Table(seven_pillars_data, colWidths=[115, 318, 90])
seven_pillars_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), primary_navy),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, bg_light]),
    ("GRID", (0, 0), (-1, -1), 0.5, border_gray),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
]))
story.append(seven_pillars_table)
story.append(Spacer(1, 8))

story.append(Paragraph("Kazanan Skoruna Göre Karar Matrisi:", h2_style))
scores_data = [
    [Paragraph("Skor Aralığı", tbl_hdr_style), Paragraph("Değerlendirme", tbl_hdr_style), Paragraph("Uygulanacak E-Ticaret Stratejisi", tbl_hdr_style)],
    [Paragraph("90 - 100 Puan", tbl_cell_bold), Paragraph("🚀 Mega Kazanan Ürün", tbl_cell_style), Paragraph("Hemen test reklamlarına çıkın. İlk 48 saatte kârlılık gelirse bütçeyi agresif şekilde dikey ve yatay ölçekleyin.", tbl_cell_style)],
    [Paragraph("75 - 89 Puan", tbl_cell_bold), Paragraph("📈 Güçlü Potansiyelli Ürün", tbl_cell_style), Paragraph("Doğru video kancası (Hook) ve 2'li paket (Bundle) indirim teklifleriyle yüksek kârlılık sağlar.", tbl_cell_style)],
    [Paragraph("60 - 74 Puan", tbl_cell_bold), Paragraph("⚠️ Orta / Niş Riskli Ürün", tbl_cell_style), Paragraph("Yalnızca çok spesifik bir alt nişe hitap eder veya marj düşüktür. Ekstra upsell eklemeden girmeyin.", tbl_cell_style)],
    [Paragraph("< 60 Puan", tbl_cell_bold), Paragraph("❌ Uzak Durulmalı", tbl_cell_style), Paragraph("Reklam maliyetlerini çıkaramaz, iade riski yüksektir. Zaman ve sermaye kaybettirir, vazgeçin.", tbl_cell_style)]
]
scores_table = Table(scores_data, colWidths=[90, 140, 293])
scores_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), royal_blue),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, bg_light]),
    ("GRID", (0, 0), (-1, -1), 0.5, border_gray),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
]))
story.append(scores_table)
story.append(Spacer(1, 8))

story.append(Paragraph("Örnek Karşılaştırma: Kazanan vs Kaybeden Ürün", h2_style))
comparison_data = [
    [Paragraph("Metrik", tbl_hdr_style), Paragraph("Kazanan Örnek: Ultrasonik Diş Temizleyici", tbl_hdr_style), Paragraph("Kaybeden Örnek: Sıradan Pamuklu Tişört", tbl_hdr_style)],
    [Paragraph("Problem", tbl_cell_bold), Paragraph("Pahalı diş hekimi masraflarını önler (Ağrı noktası: 9/10)", tbl_cell_style), Paragraph("Problem çözmez, sıradan giyim (1/10)", tbl_cell_style)],
    [Paragraph("Video Etkisi", tbl_cell_bold), Paragraph("Taş ve lekeleri 3 saniyede yok eden görüntü (9/10)", tbl_cell_style), Paragraph("Statik kumaş, parmak kaydırmayı durdurmaz (2/10)", tbl_cell_style)],
    [Paragraph("Marj Oranı", tbl_cell_bold), Paragraph("Maliyet: $5.50 | Satış: $34.99 (%84 Marj / 6.3x Çarpan)", tbl_cell_style), Paragraph("Maliyet: $9 | Satış: $18 (%50 Marj / 2.0x Çarpan - Yetersiz)", tbl_cell_style)],
    [Paragraph("Sonuç", tbl_cell_bold), Paragraph("<b>92 Puan: MEGA WINNER (Hemen Ölçekle)</b>", tbl_cell_style), Paragraph("<b>42 Puan: UZAK DUR (Reklamı Çıkaramaz)</b>", tbl_cell_style)]
]
comparison_table = Table(comparison_data, colWidths=[80, 221, 222])
comparison_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#334155")),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, bg_light]),
    ("GRID", (0, 0), (-1, -1), 0.5, border_gray),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
]))
story.append(comparison_table)

# ==========================================
# PAGE 3: GLOBAL MARKETS & AD STRATEGY
# ==========================================
story.append(PageBreak())

story.append(Paragraph("3. HEDEF ÜLKE ANALİZİ & REKLAM MECRASI STRATEJİSİ", h1_style))
story.append(Paragraph(
    "Bir ürün harika olsa bile yanlış coğrafyada ya da yanlış reklam kanalında test edilirse başarısız olur. "
    "Aşağıdaki stratejik matris, bütçenizi en yüksek dönüşüm getiren pazarlara ve platformlara kanalize eder:",
    body_style
))
story.append(Spacer(1, 6))

story.append(Paragraph("A) Bu Ürün En Çok Hangi Ülkede Tutar? (Küresel Pazar Analizi)", h2_style))
country_deep_data = [
    [Paragraph("Bölge", tbl_hdr_style), Paragraph("Öncelikli Ülkeler", tbl_hdr_style), Paragraph("Tüketici Davranışı & Lojistik Avantajı", tbl_hdr_style), Paragraph("Önemli İpucu", tbl_hdr_style)],
    [Paragraph("Tier 1 (İngilizce)", tbl_cell_bold), Paragraph("ABD, İngiltere, Kanada, Avustralya", tbl_cell_style), Paragraph("Dünyanın en yüksek dürtüsel internetten alışveriş kültürü. Stripe ve PayPal sorunsuz çalışır. Lojistik 6-10 gün.", tbl_cell_style), Paragraph("İlk testleri daima ABD'de yapın; en hızlı veri ABD'den toplanır.", tbl_cell_style)],
    [Paragraph("Tier 1 (Avrupa)", tbl_cell_bold), Paragraph("Almanya, Hollanda, İskandinavya", tbl_cell_style), Paragraph("Yüksek harcama gücü, fonksiyonel ürün merakı. Klarna, Sofort ve iDeal yerel ödemeleri şarttır.", tbl_cell_style), Paragraph("Almanca dil lokalizasyonu dönüşümü %40 artırır.", tbl_cell_style)],
    [Paragraph("Körfez (GCC)", tbl_cell_bold), Paragraph("BAE, Suudi Arabistan, Kuveyt, Katar", tbl_cell_style), Paragraph("Dünyanın en yüksek sepet tutarı (AOV). Lüks ve teknolojik ürünlere yoğun talep.", tbl_cell_style), Paragraph("Kapıda ödeme (COD) oranı yüksektir; BAE'de kart tercihi öndedir.", tbl_cell_style)],
    [Paragraph("Uzak Durulacaklar", tbl_cell_bold), Paragraph("Brezilya, Hindistan, Nijerya", tbl_cell_style), Paragraph("Yüksek gümrük vergileri, kaybolan paketler ve düşük teslimat güveni nedeniyle başlangıçta dropshipping için uygunsuzdur.", tbl_cell_style), Paragraph("Yerel deponuz yoksa kesinlikle reklam açmayın.", tbl_cell_style)]
]
country_deep_table = Table(country_deep_data, colWidths=[90, 110, 213, 110])
country_deep_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), royal_blue),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, bg_light]),
    ("GRID", (0, 0), (-1, -1), 0.5, border_gray),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
]))
story.append(country_deep_table)
story.append(Spacer(1, 8))

story.append(Paragraph("B) Reklam Mecrası Karar Matrisi (TikTok vs Meta vs Google)", h2_style))
platform_data = [
    [Paragraph("Kanal", tbl_hdr_style), Paragraph("Uygun Ürün Tipi", tbl_hdr_style), Paragraph("Hedef Kitle & Davranış", tbl_hdr_style), Paragraph("Önerilen Kampanya Tipi", tbl_hdr_style)],
    [Paragraph("TikTok Ads", tbl_cell_bold), Paragraph("Görsel yenilikler, ilginç gadget'lar, güzellik.", tbl_cell_style), Paragraph("18-35 yaş. Eğlenirken dürtüsel alışverişe en açık kitle.", tbl_cell_style), Paragraph("Spark Ads + Geniş Hedefleme (Broad CBO)", tbl_cell_style)],
    [Paragraph("Meta (Instagram/FB)", tbl_cell_bold), Paragraph("Problem çözen ürünler, anne-bebek, ortopedik.", tbl_cell_style), Paragraph("25-55 yaş. Satın alma gücü yüksek olgun kitle.", tbl_cell_style), Paragraph("Advantage+ Shopping Campaign (ASC) + Reels", tbl_cell_style)],
    [Paragraph("Google Ads / PMax", tbl_cell_bold), Paragraph("Arama hacmi olan spesifik ihtiyaçlar.", tbl_cell_style), Paragraph("Yüksek niyetli (High-intent) hazır alıcılar.", tbl_cell_style), Paragraph("Google Shopping & Responsive Search Ads", tbl_cell_style)],
    [Paragraph("Pinterest Ads", tbl_cell_bold), Paragraph("Ev dekoru, düzenleme, estetik mutfak gereçleri.", tbl_cell_style), Paragraph("%70+ kadın kitle, planlı ve kaliteli alışveriş.", tbl_cell_style), Paragraph("Dikey Video Pinler & Karusel Alışveriş", tbl_cell_style)]
]
platform_table = Table(platform_data, colWidths=[90, 140, 163, 130])
platform_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), primary_navy),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, bg_light]),
    ("GRID", (0, 0), (-1, -1), 0.5, border_gray),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
]))
story.append(platform_table)
story.append(Spacer(1, 8))

story.append(Paragraph("C) 3 Saniyelik Viral Video Reklam Şablonu (High-Converting UGC)", h2_style))
ugc_data = [
    [Paragraph("Zaman Dilimi", tbl_hdr_style), Paragraph("Bölüm", tbl_hdr_style), Paragraph("Psikolojik Taktik & Sahne Kurgusu", tbl_hdr_style)],
    [Paragraph("0:00 - 0:03", tbl_cell_bold), Paragraph("Kanca (Hook)", tbl_cell_style), Paragraph("<b>1. Merak Kancası:</b> 'TikTok'ta herkesin bahsettiği bu alet gerçekten çalışıyor mu?'<br/><b>2. Acı / Korku Kancası:</b> 'Bunu sipariş etmeden önce neden kimse beni uyarmadı?'<br/><b>3. Karşılaştırma Kancası:</b> 'Eski can sıkıcı yöntem vs Yeni 3 saniyelik pratik çözüm!'", tbl_cell_style)],
    [Paragraph("0:04 - 0:18", tbl_cell_bold), Paragraph("Problem & Çözüm", tbl_cell_style), Paragraph("Eski yöntemin ne kadar yorucu olduğunu gösterin, ardından ürünün devreye girip sorunu nasıl saniyeler içinde ortadan kaldırdığını yakın çekimle demonstrasyon yapın.", tbl_cell_style)],
    [Paragraph("0:19 - 0:24", tbl_cell_bold), Paragraph("Sosyal Kanıt", tbl_cell_style), Paragraph("'40.000+ mutlu müşteri yanılıyor olamaz!' + 5 yıldızlı müşteri yorumunun ekrana yerleştirilmesi.", tbl_cell_style)],
    [Paragraph("0:25 - 0:30", tbl_cell_bold), Paragraph("Harekete Geç (CTA)", tbl_cell_style), Paragraph("'Bugüne özel %50 İndirim + Ücretsiz Kargo fırsatı tükenmek üzere! Hemen profildeki linke tıklayın.'", tbl_cell_style)]
]
ugc_table = Table(ugc_data, colWidths=[70, 95, 358])
ugc_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), accent_blue),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, bg_light]),
    ("GRID", (0, 0), (-1, -1), 0.5, border_gray),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
]))
story.append(ugc_table)

# ==========================================
# PAGE 4: UNIT ECONOMICS & MULTI-AI SETUP
# ==========================================
story.append(PageBreak())

story.append(Paragraph("4. FİNANSAL BİRİM MALİYET (UNIT ECONOMICS) & ÇOKLU PLATFORM MCP KURULUMU", h1_style))
story.append(Paragraph(
    "Bir e-ticaret markasının sürdürülebilir kârlılığı, santimi santimine hesaplanmış birim maliyet analizine dayanır. "
    "Aşağıdaki formüller ve örnek senaryo, reklam bütçenizi kontrol altında tutmanın temel kuralıdır:",
    body_style
))
story.append(Spacer(1, 6))

story.append(Paragraph("A) Başa Baş (Break-Even) ROAS ve Max CPA Hesaplama Modeli", h2_style))
unit_econ_calc_data = [
    [Paragraph("Finansal Kalem", tbl_hdr_style), Paragraph("Formül / Tanım", tbl_hdr_style), Paragraph("Örnek Hesap ($29.99 Satış)", tbl_hdr_style)],
    [Paragraph("Satış Fiyatı (AOV)", tbl_cell_bold), Paragraph("Müşterinin mağazada ödediği perakende tutar", tbl_cell_style), Paragraph("$29.99", tbl_cell_bold)],
    [Paragraph("Tedarik + Kargo (COGS)", tbl_cell_bold), Paragraph("Fabrika maliyeti + kapıya teslim kargo navlunu", tbl_cell_style), Paragraph("$6.50", tbl_cell_style)],
    [Paragraph("Ödeme Komisyonu", tbl_cell_bold), Paragraph("Stripe / PayPal işlem ücreti (%3.5 + $0.30)", tbl_cell_style), Paragraph("$1.35", tbl_cell_style)],
    [Paragraph("Brüt Kâr (Before Ads)", tbl_cell_bold), Paragraph("Satış Fiyatı - (COGS + Ödeme Komisyonu)", tbl_cell_style), Paragraph("<b>$22.14 (%73.8 Brüt Marj)</b>", tbl_cell_style)],
    [Paragraph("Başa Baş ROAS (Break-even)", tbl_cell_bold), Paragraph("Satış Fiyatı / Brüt Kâr", tbl_cell_style), Paragraph("<b>1.35x (Bu oranın üstü net kârdır)</b>", tbl_cell_style)],
    [Paragraph("Maksimum İzin Verilen CPA", tbl_cell_bold), Paragraph("Sipariş başına reklama ödenebilecek azami maliyet", tbl_cell_style), Paragraph("<b>$22.14 (Bunu aşarsa reklam durdurulur)</b>", tbl_cell_style)]
]
unit_econ_table = Table(unit_econ_calc_data, colWidths=[120, 243, 160])
unit_econ_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), emerald_green),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, bg_light]),
    ("GRID", (0, 0), (-1, -1), 0.5, border_gray),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
]))
story.append(unit_econ_table)
story.append(Spacer(1, 8))

story.append(Paragraph("B) Çoklu Yapay Zeka Kurulum Rehberi (Cross-Platform)", h2_style))
mcp_platform_data = [
    [Paragraph("Platform", tbl_hdr_style), Paragraph("Kurulum Türü", tbl_hdr_style), Paragraph("Tek Tıkla Entegrasyon Adımı", tbl_hdr_style)],
    [Paragraph("Google Antigravity & Gemini", tbl_cell_bold), Paragraph("Native Skill", tbl_cell_style), Paragraph("<code>.gemini/skills/sales-manager/SKILL.md</code> hazır. Sohbete doğrudan <code>/sales-manager</code> yazın.", tbl_cell_style)],
    [Paragraph("Claude Desktop", tbl_cell_bold), Paragraph("MCP Stdio Server", tbl_cell_style), Paragraph("<code>claude_desktop_config.json</code> içine node index.js MCP yolunu ekleyin.", tbl_cell_style)],
    [Paragraph("Claude Code (CLI)", tbl_cell_bold), Paragraph("MCP CLI & Slash", tbl_cell_style), Paragraph("<code>claude mcp add sales-manager node [path]/mcp-server/dist/index.js</code> komutunu çalıştırın.", tbl_cell_style)],
    [Paragraph("Cursor IDE & Windsurf", tbl_cell_bold), Paragraph("Agent MCP & Rules", tbl_cell_style), Paragraph("Cursor Settings -> Features -> MCP Servers altına command olarak <code>node dist/index.js</code> ekleyin.", tbl_cell_style)],
    [Paragraph("ChatGPT / Custom GPTs / Codex", tbl_cell_bold), Paragraph("System Instructions", tbl_cell_style), Paragraph("Custom GPT Instructions kısmına <code>configs/chatgpt_custom_gpt_instructions.txt</code> metnini yapıştırın.", tbl_cell_style)]
]
mcp_platform_table = Table(mcp_platform_data, colWidths=[120, 100, 303])
mcp_platform_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), primary_navy),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, bg_light]),
    ("GRID", (0, 0), (-1, -1), 0.5, border_gray),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
]))
story.append(mcp_platform_table)
story.append(Spacer(1, 10))

# FINAL INSTITUTIONAL FOOTER CARD
summary_card_data = [
    [Paragraph("🚀 AÇIK KAYNAK KOD & KATKI SAĞLAMA", ParagraphStyle("WhiteHdr", fontName="Arial-Bold", fontSize=10, textColor=colors.white, alignment=1))],
    [Paragraph(
        "AI Sales Director sistemi tamamen açık kaynaklıdır (MIT Lisansı). "
        "Kaynak kodları incelemek, MCP sunucusunu kendi projelerinize entegre etmek veya katkı sunmak için resmi depoyu ziyaret edebilirsiniz:<br/>"
        "<font color='#BFDBFE'><b>GitHub: https://github.com/EthYusuf/ai-sales-director</b></font><br/>"
        "Geliştirici: <b>EthYusuf</b> | Sürüm: <b>1.0.0 Production</b>",
        ParagraphStyle("WhiteBody", fontName="Arial", fontSize=8.5, leading=12, textColor=colors.HexColor("#F1F5F9"), alignment=1)
    )]
]
summary_card_table = Table(summary_card_data, colWidths=[523])
summary_card_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), royal_blue),
    ("PADDING", (0, 0), (-1, -1), 8),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
]))
story.append(summary_card_table)

doc.build(story, canvasmaker=NumberedCanvas)
print("Institutional 4-page PDF successfully built:", pdf_filename)
