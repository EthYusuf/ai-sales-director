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

MCP kurulu değilse, standart **Uzman E-Ticaret Değerlendirme Çerçevesini** kullanarak eksiksiz bir rapor sunun.
