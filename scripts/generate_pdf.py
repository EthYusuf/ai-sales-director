import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register Arial with full Turkish character support
font_path = "C:/Windows/Fonts/arial.ttf"
font_bold_path = "C:/Windows/Fonts/arialbd.ttf"
pdfmetrics.registerFont(TTFont("Arial", font_path))
pdfmetrics.registerFont(TTFont("Arial-Bold", font_bold_path))

pdf_filename = "AI_Sales_Director_Master_Guide.pdf"
doc = SimpleDocTemplate(
    pdf_filename,
    pagesize=A4,
    leftMargin=36,
    rightMargin=36,
    topMargin=36,
    bottomMargin=36
)

styles = getSampleStyleSheet()

# Custom styles
primary_color = colors.HexColor("#0F172A") # Deep Slate
brand_blue = colors.HexColor("#1E40AF")    # Royal Blue
accent_cyan = colors.HexColor("#0284C7")   # Sky Blue
emerald_green = colors.HexColor("#059669") # Success Emerald
bg_light = colors.HexColor("#F8FAFC")      # Slate 50
border_gray = colors.HexColor("#E2E8F0")

title_style = ParagraphStyle(
    "DocTitle",
    fontName="Arial-Bold",
    fontSize=22,
    leading=26,
    textColor=colors.white,
    alignment=1
)

subtitle_style = ParagraphStyle(
    "DocSubtitle",
    fontName="Arial",
    fontSize=11,
    leading=15,
    textColor=colors.HexColor("#93C5FD"),
    alignment=1
)

h1_style = ParagraphStyle(
    "Header1",
    fontName="Arial-Bold",
    fontSize=14,
    leading=18,
    textColor=brand_blue,
    spaceBefore=12,
    spaceAfter=6
)

h2_style = ParagraphStyle(
    "Header2",
    fontName="Arial-Bold",
    fontSize=11,
    leading=15,
    textColor=primary_color,
    spaceBefore=8,
    spaceAfter=4
)

body_style = ParagraphStyle(
    "Body",
    fontName="Arial",
    fontSize=9.5,
    leading=13.5,
    textColor=colors.HexColor("#334155")
)

bullet_style = ParagraphStyle(
    "BulletText",
    fontName="Arial",
    fontSize=9,
    leading=13,
    textColor=colors.HexColor("#1E293B")
)

table_header_style = ParagraphStyle(
    "TableHeader",
    fontName="Arial-Bold",
    fontSize=9,
    leading=12,
    textColor=colors.white
)

table_body_style = ParagraphStyle(
    "TableBody",
    fontName="Arial",
    fontSize=8.5,
    leading=11.5,
    textColor=colors.HexColor("#1E293B")
)

story = []

# --- HEADER BANNER ---
header_data = [
    [Paragraph("AI SALES DIRECTOR (/sales-manager)", title_style)],
    [Paragraph("E-Ticaret Kazanan Ürün Keşfi, Küresel Hedef Pazar Analizi & Viral Reklam Stratejisi El Kitabı", subtitle_style)],
    [Paragraph("Evrensel MCP Server & Multi-Platform Yapay Zeka Skilli | GitHub: EthYusuf/ai-sales-director", subtitle_style)]
]
header_table = Table(header_data, colWidths=[523])
header_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), brand_blue),
    ("TOPPADDING", (0, 0), (-1, -1), 12),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
    ("LEFTPADDING", (0, 0), (-1, -1), 15),
    ("RIGHTPADDING", (0, 0), (-1, -1), 15),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
]))
story.append(header_table)
story.append(Spacer(1, 14))

# --- GİRİŞ & PROBLEM TANIMI ---
story.append(Paragraph("1. GİRİŞ: E-Ticarette Neden İnsanların %90'ı Para Kaybediyor?", h1_style))
story.append(Paragraph(
    "E-ticaret ve dropshipping girişimcilerinin en büyük yanılgısı, ürün seçimini kişisel beğenilere göre yapmaktır. "
    "Binlerce dolar reklam bütçesi harcandıktan sonra ürünün 'vay canına' etkisinin olmadığı, kargo maliyetlerinin kârı erittiği, "
    "veya yanlış ülkede/yanlış platformda reklam verildiği anlaşılır. <b>AI Sales Director (/sales-manager)</b>, "
    "bu süreci şansa bırakmaz; 5 aşamalı algoritmik bir e-ticaret denetimi uygulayarak ürünü daha teste sokmadan onaylar veya eler.",
    body_style
))
story.append(Spacer(1, 10))

# --- BÖLÜM 2: 7 ALTIN KURAL ---
story.append(Paragraph("2. KAZANAN ÜRÜN DEĞERLENDİRMESİNİN 7 ALTIN KURALI (THE 7 PILLARS)", h1_style))
pillars_data = [
    [Paragraph("Kriter", table_header_style), Paragraph("Açıklama", table_header_style), Paragraph("Kazanan Eşik Değeri", table_header_style)],
    [Paragraph("1. Acı / Problem Çözme", table_body_style), Paragraph("İnsanların canını sıkan, zaman ya da para kaybettiren bir sorunu çözmeli.", table_body_style), Paragraph("Ağrıyı dindiren ürünler dürtüsel satar.", table_body_style)],
    [Paragraph("2. Scroll-Stopping Wow Faktörü", table_body_style), Paragraph("TikTok veya Reels akışında ilk 3 saniyede izleyiciyi ekrana kilitlemeli.", table_body_style), Paragraph("Öncesi/Sonrası etkisi yüksek olmalı.", table_body_style)],
    [Paragraph("3. 3x Marj Kuralı", table_body_style), Paragraph("Satış fiyatı, toplam tedarik ve kargo maliyetinin en az 3 katı olmalıdır.", table_body_style), Paragraph("Minimum %65-%75 brüt kâr marjı.", table_body_style)],
    [Paragraph("4. Yerelde Kolay Bulunamama", table_body_style), Paragraph("Müşteri bu ürünü mahalle marketinden veya AVM'den raftan alamamalı.", table_body_style), Paragraph("Özel, yenilikçi ve niş olmalı.", table_body_style)],
    [Paragraph("5. Kargo & Lojistik Kolaylığı", table_body_style), Paragraph("500 gramdan hafif, kırılmaz ve gümrük kısıtlamasına tabi olmamalı.", table_body_style), Paragraph("İade oranı %3'ün altında kalmalı.", table_body_style)],
    [Paragraph("6. UGC ve İçerik Uygunluğu", table_body_style), Paragraph("Gerçek kullanıcı videoları (UGC) ve demonstrasyona uygun olmalı.", table_body_style), Paragraph("Kamera karşısında anlatımı kolay.", table_body_style)],
    [Paragraph("7. Geniş Pazar Kitlesi", table_body_style), Paragraph("Yalnızca birkaç bin kişiye değil, yüz binlerce potansiyel müşteriye hitap etmeli.", table_body_style), Paragraph("Ölçeklenebilir kitle potansiyeli.", table_body_style)]
]
pillars_table = Table(pillars_data, colWidths=[120, 260, 143])
pillars_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), primary_color),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, bg_light]),
    ("GRID", (0, 0), (-1, -1), 0.5, border_gray),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
]))
story.append(pillars_table)
story.append(Spacer(1, 12))

# --- BÖLÜM 3: HEDEF ÜLKELER ---
story.append(Paragraph("3. HEDEF ÜLKE ANALİZİ: BU ÜRÜN EN ÇOK HANGİ ÜLKEDE TUTAR?", h1_style))
country_data = [
    [Paragraph("Pazar Grubu", table_header_style), Paragraph("Öne Çıkan Ülkeler", table_header_style), Paragraph("Neden Bu Pazar & Stratejik Avantaj", table_header_style)],
    [Paragraph("Tier 1 (Lider Pazarlar)", table_body_style), Paragraph("ABD, İngiltere, Kanada, Avustralya", table_body_style), Paragraph("Dünyanın en yüksek dürtüsel satın alma oranı. Stripe sorunsuz çalışır. Avustralya ters mevsim avantajı sunar.", table_body_style)],
    [Paragraph("Tier 1 (Kıta Avrupası)", table_body_style), Paragraph("Almanya, Hollanda, İskandinavya", table_body_style), Paragraph("Kaliteli problem çözen ürünleri severler. Yerel ödeme yöntemleri (Klarna, Sofort, iDeal) eklenirse dönüşüm %40 artar.", table_body_style)],
    [Paragraph("Yüksek Harcama (GCC)", table_body_style), Paragraph("BAE, Suudi Arabistan, Kuveyt, Katar", table_body_style), Paragraph("Kişi başı harcama gücü rekor seviyededir. Lüks ve estetik ürünlerde sepet ortalaması (AOV) çok yüksektir.", table_body_style)],
    [Paragraph("Kaçınılması Gerekenler", table_body_style), Paragraph("Hindistan, Brezilya, Nijerya, İtalya (dil yoksa)", table_body_style), Paragraph("Yüksek gümrük vergileri, teslim edilmeme riski, yüksek iade oranı ve düşük ödeme güveni.", table_body_style)]
]
country_table = Table(country_data, colWidths=[110, 130, 283])
country_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), brand_blue),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, bg_light]),
    ("GRID", (0, 0), (-1, -1), 0.5, border_gray),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
]))
story.append(country_table)
story.append(Spacer(1, 14))

# PAGE BREAK FOR CRISP LAYOUT
story.append(PageBreak())

# --- BÖLÜM 4: REKLAM MECRASI VE VİRAL SENARYO ---
story.append(Paragraph("4. REKLAM MECRASI KARAR MATRİSİ & VİRAL SENARYO KURGUSU", h1_style))
story.append(Paragraph(
    "Ürünün türüne göre doğru reklam platformunu seçmek, harcanan her kuruşun kâra dönüşmesini sağlar:",
    body_style
))
story.append(Spacer(1, 6))

ad_data = [
    [Paragraph("Platform", table_header_style), Paragraph("Hangi Ürün Tipleri İçin?", table_header_style), Paragraph("En İyi Reklam Formatı", table_header_style)],
    [Paragraph("TikTok Ads & UGC", table_body_style), Paragraph("Görsel yenilikler, 'Vay canına' dedirten aletler, 18-35 yaş kitlesi.", table_body_style), Paragraph("Spark Ads, gerçek kullanıcı deneyimi hissi veren dikey 9:16 videolar.", table_body_style)],
    [Paragraph("Meta (Instagram/FB)", table_body_style), Paragraph("Problem çözen ürünler, anne-bebek, ev-yaşam, 25-55 yaş kitlesi.", table_body_style), Paragraph("Advantage+ Alışveriş Kampanyası (ASC), Reels, Öncesi/Sonrası kurguları.", table_body_style)],
    [Paragraph("Google Ads / Shopping", table_body_style), Paragraph("İnsanların halihazırda arama motoruna yazdığı spesifik ihtiyaç ürünleri.", table_body_style), Paragraph("Google Shopping, Performance Max, Yüksek niyetli arama reklamları.", table_body_style)],
    [Paragraph("Pinterest Ads", table_body_style), Paragraph("Ev dekorasyonu, estetik mutfak, hediye nişleri (%70+ kadın kitle).", table_body_style), Paragraph("Estetik Video Pinler, oda dönüşüm videoları.", table_body_style)]
]
ad_table = Table(ad_data, colWidths=[100, 210, 213])
ad_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), primary_color),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, bg_light]),
    ("GRID", (0, 0), (-1, -1), 0.5, border_gray),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
]))
story.append(ad_table)
story.append(Spacer(1, 10))

story.append(Paragraph("Yüksek Dönüşümlü 3 Aşamalı Video Reklam Şablonu (30 Saniye)", h2_style))
video_framework_data = [
    [Paragraph("Süre", table_header_style), Paragraph("Bölüm", table_header_style), Paragraph("Psikolojik Hedef & Sahne Detayı", table_header_style)],
    [Paragraph("0:00 - 0:03", table_body_style), Paragraph("Kanca (Hook)", table_body_style), Paragraph("İzleyiciyi durdur. Merak, acı veya 'Bunu almadan önce neden kimse beni uyarmadı?' açısı.", table_body_style)],
    [Paragraph("0:04 - 0:18", table_body_style), Paragraph("Problem & Çözüm", table_body_style), Paragraph("Problemin can sıkıcılığını göster, ardından ürünün bunu 2 saniyede nasıl çözdüğünü canlandır.", table_body_style)],
    [Paragraph("0:19 - 0:24", table_body_style), Paragraph("Sosyal Kanıt", table_body_style), Paragraph("'50.000+ mutlu müşteri yanılıyor olamaz!' + 5 yıldızlı müşteri yorumu görseli.", table_body_style)],
    [Paragraph("0:25 - 0:30", table_body_style), Paragraph("Harekete Geç (CTA)", table_body_style), Paragraph("'Bugüne özel %50 İndirim + Ücretsiz Kargo! Profildeki linke tıkla.' (Aciliyet hissi ver).", table_body_style)]
]
video_table = Table(video_framework_data, colWidths=[70, 100, 353])
video_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), accent_cyan),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, bg_light]),
    ("GRID", (0, 0), (-1, -1), 0.5, border_gray),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
]))
story.append(video_table)
story.append(Spacer(1, 14))

# --- BÖLÜM 5: FİNANSAL BİRİM MALİYET (UNIT ECONOMICS) ---
story.append(Paragraph("5. FİNANSAL BİRİM MALİYET (UNIT ECONOMICS) & BAŞA BAŞ ROAS", h1_style))
story.append(Paragraph(
    "Bir e-ticaret işletmesinin batmaması için reklam harcamalarının başa baş (Break-Even) noktasını bilmesi şarttır:",
    body_style
))
story.append(Spacer(1, 6))

formula_text = """
<b>Başa Baş (Break-Even) ROAS Formülü:</b><br/>
• Brüt Kâr = Satış Fiyatı - (Ürün Tedarik Maliyeti + Kargo + Ödeme Altyapı Komisyonu)<br/>
• Başa Baş ROAS = Satış Fiyatı / Brüt Kâr<br/>
• Maksimum İzin Verilen CPA = Brüt Kâr (Müşteri edinmek için reklama ödenebilecek azami tutar)
"""
formula_data = [[Paragraph(formula_text, body_style)]]
formula_table = Table(formula_data, colWidths=[523])
formula_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#EFF6FF")),
    ("BOX", (0, 0), (-1, -1), 1, brand_blue),
    ("PADDING", (0, 0), (-1, -1), 8),
]))
story.append(formula_table)
story.append(Spacer(1, 14))

# --- BÖLÜM 6: ÇOKLU YAPAY ZEKA KURULUMU & GITHUB ---
story.append(Paragraph("6. ÇOKLU PLATFORM KURULUMU & GITHUB ERİŞİMİ", h1_style))
story.append(Paragraph(
    "Bu sistem tüm popüler yapay zeka araçlarıyla tak-çalıştır (Plug & Play) uyumludur. "
    "Aşağıdaki araçlardan dilediğinize saniyeler içinde ekleyebilirsiniz:",
    body_style
))
story.append(Spacer(1, 6))

setup_data = [
    [Paragraph("Platform", table_header_style), Paragraph("Kurulum Yöntemi", table_header_style)],
    [Paragraph("Antigravity & Gemini CLI", table_body_style), Paragraph("Çalışma alanında <code>.gemini/skills/sales-manager/SKILL.md</code> hazır. <code>/sales-manager</code> yazın.", table_body_style)],
    [Paragraph("Claude Desktop", table_body_style), Paragraph("<code>claude_desktop_config.json</code> dosyasına node index.js MCP yolunu ekleyin.", table_body_style)],
    [Paragraph("Claude Code (CLI)", table_body_style), Paragraph("<code>claude mcp add sales-manager node [path]/mcp-server/dist/index.js</code> komutunu çalıştırın.", table_body_style)],
    [Paragraph("Cursor & Windsurf IDE", table_body_style), Paragraph("Cursor Settings -> MCP -> Add Server ile <code>node dist/index.js</code> komutunu girin.", table_body_style)],
    [Paragraph("OpenAI ChatGPT / GPTs", table_body_style), Paragraph("Custom GPT oluşturup <code>chatgpt_custom_gpt_instructions.txt</code> metnini talimat olarak yapıştırın.", table_body_style)]
]
setup_table = Table(setup_data, colWidths=[150, 373])
setup_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), primary_color),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, bg_light]),
    ("GRID", (0, 0), (-1, -1), 0.5, border_gray),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
]))
story.append(setup_table)
story.append(Spacer(1, 14))

# FOOTER BANNER
footer_text = Paragraph(
    "<b>Açık Kaynak Kod Deposu:</b> <font color='#1E40AF'><u>https://github.com/EthYusuf/ai-sales-director</u></font><br/>"
    "Geliştirici: EthYusuf | Lisans: MIT | Sürüm: 1.0.0",
    ParagraphStyle("Footer", fontName="Arial", fontSize=8.5, leading=12, alignment=1, textColor=colors.HexColor("#64748B"))
)
story.append(footer_text)

doc.build(story)
print("PDF successfully generated:", pdf_filename)
