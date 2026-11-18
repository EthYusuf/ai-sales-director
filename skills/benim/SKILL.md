---
name: benim
description: E-Ticaret Kazanan Ürün Avcısı, Küresel Hedef Pazar Analizi ve Viral Reklam Stratejisi (TikTok, Meta, Google). /benim komutu ile tetiklenir.
---

# 🚀 E-Ticaret Kazanan Ürün & Reklam Stratejisi Skilli (/benim)

Bu skill, kullanıcı e-ticaret (Dropshipping, Private Label, D2C) için ürün araştırması yaptığında veya `/benim` komutunu kullandığında devreye girer. İnsanların "Bu ürün satar mı?", "En çok hangi ülkede tutar?", "Reklamını nereye (TikTok, Instagram, Google) atmalıyım?" ve "Kârlı mı?" sorularını veriye dayalı profesyonel bir çerçeveyle yanıtlar.

---

## 🎯 Komut Tetikleyicisi: `/benim`
Kullanıcı mesajına `/benim` veya `/benim <ürün adı / link / niş>` ile başladığında şu 5 aşamalı e-ticaret analizi sırasıyla uygulanır:

1. **Ürün Uygunluk & Kazanan Puanı (Winning Score 0-100)**
2. **Finansal Birim Maliyet & Başa Baş ROAS (Unit Economics)**
3. **Hedef Ülke & Küresel Pazar Uygunluğu (Tier 1, GCC, vb.)**
4. **Reklam Platformu Kararı (TikTok vs Meta vs Google Ads)**
5. **Viral Video Reklam Senaryosu (Hook, Problem-Çözüm, CTA)**

Eğer ortamda **MCP Server** (`ecommerce-winning-product-hunter`) kurulu ise ilgili MCP araçlarını çağırın:
- `analyze_product_viability`
- `recommend_target_countries`
- `generate_ad_channel_strategy`
- `calculate_ecommerce_unit_economics`
- `get_ecommerce_playbook`

MCP kurulu değilse, aşağıdaki **Uzman E-Ticaret Değerlendirme Çerçevesini** kullanarak eksiksiz bir rapor sunun.

---

## 📊 1. ADIM: Kazanan Ürün Analizi (The 7 Pillars)
Ürünü şu 7 kritere göre puanlayın ve 100 üzerinden bir skor verin:
1. **Problem Çözme Gücü (Ağrı Noktası):** İnsanların canını sıkan, zaman veya para kaybettiren bir şeyi çözüyor mu?
2. **"Vay Canına" (Wow-Factor) Etkisi:** İlk 3 saniyede parmak kaydırmayı durduran görsel/tatmin edici bir tarafı var mı?
3. **Fiyat ve Marj Sağlığı:** Satış fiyatı, tedarik maliyetinin en az 3 katı (3x kuralı) olabiliyor mu?
4. **Yerel Mağazada Kolay Bulunamama:** Müşteri markete gidip bunu hemen raftan alabiliyor mu?
5. **Kargo & Lojistik Feasibility:** 500 gramdan hafif mi? Kırılabilir cam, sıvı veya patlayıcı batarya riski var mı?
6. **İçerik Üretilebilirliği (UGC Uygunluğu):** Öncesi/sonrası, kutu açılışı veya eğlenceli kullanım senaryoları çekilebilir mi?
7. **Pazar Genişliği:** Kitle çok mu dar, yoksa milyonlarca insana satılabilir mi?

**Karar:**
- `90 - 100 Puan`: 🚀 **Mega Kazanan Ürün (Scale Fast)**
- `75 - 89 Puan`: 📈 **Güçlü Potansiyel (Doğru kanca ile kârlı)**
- `60 - 74 Puan`: ⚠️ **Orta / Niş Riskli (Bundle veya özel kurgu gerekir)**
- `< 60 Puan`: ❌ **Uzak Durulmalı (Reklam maliyetlerini çıkaramaz)**

---

## 🌍 2. ADIM: Bu Ürün En Çok Hangi Ülkede Tutar?
Ürünün fiyatına ve doğasına göre pazar haritası çıkarın:

- **Tier 1 Pazarlar (En Yüksek Harcama Gücü):**
  - **ABD (US):** Dürtüsel satın alma kralı, en yüksek hacim, en hızlı veri.
  - **İngiltere (UK):** Hızlı kargo teslimatı, güçlü internetten alma refleksi, £ kuru avantajı.
  - **Kanada & Avustralya (CA/AU):** ABD'den daha düşük CPM, yüksek sepet tutarı. (Avustralya ters mevsim avantajı sağlar!).
  - **Almanya & Hollanda (DE/NL):** Fonksiyonel ve kaliteli ürünleri sever; yerel ödeme (Klarna/Sofort/iDeal) şarttır.
- **Körfez Pazarı (GCC - BAE, Suudi Arabistan, Kuveyt):**
  - Lüks, yenilikçi gadget'lar ve güzellik ürünleri için rekor sepet ortalaması. Kapıda ödeme (COD) veya Stripe.
- **İlk Aşamada Kaçınılması Gereken Ülkeler:**
  - Yüksek gümrük vergisi, paket kaybolma riski veya yüksek iade oranına sahip ülkeleri belirtin.

---

## 📱 3. ADIM: Reklam Nereye Atılmalı? (Mecra Kararı)
Ürünün karakterine göre en doğru kanalı seçin ve nedenini açıklayın:

1. **TikTok Ads & TikTok Organik:**
   - *Ne Zaman Seçilmeli:* 18-35 yaş kitlesi, görsel wow faktörü olan, eğlenceli, demonstrasyonu tatmin edici ürünler.
   - *Format:* Spark Ads, UGC (kullanıcı deneyimi gibi görünen doğal videolar).
2. **Meta (Instagram Reels & Facebook Feed):**
   - *Ne Zaman Seçilmeli:* 25-55 yaş kitlesi, problem çözen, medikal/ergonomik, ev eşyası veya anne-bebek ürünleri.
   - *Format:* Advantage+ Alışveriş Kampanyası (ASC), Reels, Karusel.
3. **Google Ads (Shopping & Performance Max):**
   - *Ne Zaman Seçilmeli:* İnsanların problemini zaten bilip arama motoruna yazdığı ürünler (Örn: "ortopedik dizlik", "yedek filtre").
4. **Pinterest Ads:**
   - *Ne Zaman Seçilmeli:* Ev dekoru, kadın modası, mutfak düzeni, estetik hediye nişleri.

---

## 🎬 4. ADIM: Kazanan Video Reklam Senaryosu (Hook - Problem - CTA)
Kullanıcıya hemen bir içerik üreticisine (UGC Creator) gönderebileceği veya CapCut ile montajlayabileceği hazır senaryo verin:

- **0:00 - 0:03 (Kanca / Hook):** 3 Farklı alternatif (Merak, Korku/Acı, Karşılaştırma).
- **0:04 - 0:15 (Gövde / Problem & Çözüm):** Hayatı nasıl kolaylaştırdığının gösterilmesi + 3 temel fayda.
- **0:16 - 0:22 (Sosyal Kanıt):** "10.000+ kişi neden bunu kullanıyor?" + Müşteri yorumu ekran görüntüsü.
- **0:23 - 0:30 (CTA):** "Sadece bu haftaya özel %50 İndirim + Ücretsiz Kargo, profil linkinde!"

---

## 💰 5. ADIM: Finansal Birim Analizi (Unit Economics)
Kullanıcının zarar etmemesi için net formüller:
- **Satış Fiyatı:** Hedef Fiyat
- **Ürün + Kargo Maliyeti (COGS):** Tedarik Maliyeti
- **Ödeme Altyapı Komisyonu:** ~%3.5
- **Brüt Kâr:** Satış Fiyatı - Tüm Maliyetler
- **Başa Baş ROAS (Break-even ROAS):** `Satış Fiyatı / Brüt Kâr`
- **Maksimum İzin Verilen CPA (Müşteri Edinme Maliyeti):** Bu tutarın üzerindeki reklam harcamasında reklam durdurulmalıdır!
