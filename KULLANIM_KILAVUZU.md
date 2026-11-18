# 🛒 E-Ticaret Kazanan Ürün Avcısı & Küresel Reklam Stratejisi
## `/benim` Skilli & Profesyonel MCP Server Kurulum ve Kullanım Kılavuzu

Bu paket; e-ticaret (Dropshipping, Private Label, D2C) yapan girişimcilerin en büyük sorunu olan **"Hangi ürün tutar?", "Bu ürün en çok hangi ülkede satar?", "Reklamı TikTok'a mı yoksa Instagram'a mı atmalıyım?" ve "Kâr marjım beni kurtarır mı?"** sorularını veriye dayalı formüllerle çözen evrensel bir yapay zeka sistemidir.

---

## 🌟 Neler İçerir?

1. **Evrensel MCP (Model Context Protocol) Sunucusu:**
   - `analyze_product_viability`: 6 temel metrik ve 7 altın kural üzerinden 100 puanlık kazanan ürün skoru.
   - `recommend_target_countries`: Satın alma gücü, gümrük, iade oranı ve mevsimselliğe göre en kârlı ülkeleri (Tier 1, GCC vb.) belirler.
   - `generate_ad_channel_strategy`: Ürün türüne göre TikTok Ads, Meta (Instagram/FB), Google Shopping veya Pinterest önceliğini seçer ve ilk 3 saniyelik viral video kancası (Hook) ile 30 saniyelik reklam senaryosu yazar.
   - `calculate_ecommerce_unit_economics`: COGS, kargo, ödeme komisyonu, brüt marj, başa baş (Break-even) ROAS ve izin verilen maksimum müşteri edinme maliyetini (Max CPA) hesaplar.
   - `get_ecommerce_playbook`: Rakipleri casuslama (Meta Ad Library, TikTok Creative Center), test ve bütçe ölçekleme kuralları.

2. **`/benim` Komut ve Beceri (Skill) Tanımı:**
   - Tüm yapay zeka araçlarında `/benim <ürün adı veya link>` yazıldığında otomatik olarak 5 adımlı detaylı e-ticaret analiz raporunu başlatır.

---

## 🚀 Farklı Yapay Zeka Araçlarına Aktarma (Kurulum Rehberi)

### 1. Antigravity & Gemini
- Zaten bu çalışma alanında `.gemini/skills/benim/SKILL.md` olarak tanımlandı.
- Sohbete doğrudan `/benim [Ürün Adı]` yazmanız yeterlidir!

### 2. Claude Desktop (Mac / Windows)
1. Claude Desktop uygulamasında `Ayarlar (Settings) -> Developer -> Edit Config` seçeneğine tıklayın.
2. Açılan `claude_desktop_config.json` dosyasını `configs/claude_desktop_config.json` içeriği ile güncelleyin:
```json
{
  "mcpServers": {
    "ecommerce-hunter": {
      "command": "node",
      "args": [
        "C:/Users/yusuf/OneDrive/Desktop/printtomoney/autormaiton/mcp-server/dist/index.js"
      ]
    }
  }
}
```
3. Claude Desktop'ı yeniden başlatın. Çekiç (Tools) simgesinde MCP araçlarının aktif olduğunu göreceksiniz.

### 3. Claude Code (Terminal)
- Proje kökündeki `.claude/commands/benim.md` dosyası sayesinde terminalde `claude` çalıştırdığınızda doğrudan `/benim` komutunu kullanabilirsiniz.
- MCP Server'ı eklemek için terminalde:
```bash
claude mcp add ecommerce-hunter node C:/Users/yusuf/OneDrive/Desktop/printtomoney/autormaiton/mcp-server/dist/index.js
```

### 4. Cursor & Windsurf IDE
1. Cursor'da **Settings -> Features -> MCP Servers -> Add New MCP Server** yolunu izleyin:
   - **Name:** `ecommerce-hunter`
   - **Type:** `command`
   - **Command:** `node C:/Users/yusuf/OneDrive/Desktop/printtomoney/autormaiton/mcp-server/dist/index.js`
2. Ayrıca çalışma alanınızdaki `.cursorrules` dosyası Cursor Agent'ın `/benim` komutunu ve kurallarını otomatik çalıştırmasını sağlar.

### 5. OpenAI ChatGPT / Custom GPTs / Codex
1. [chatgpt.com](https://chatgpt.com) -> **Explore GPTs -> Create a GPT** deyin.
2. **Instructions (Talimatlar)** bölümüne `configs/chatgpt_custom_gpt_instructions.txt` dosyasındaki metni kopyalayıp yapıştırın.
3. GPT'nizin adını **"Winning Product Hunter (/benim)"** yapın ve kaydedin. Artık web ve mobil ChatGPT'de ürün analizi yapabilirsiniz!

---

## 🧪 Örnek Kullanım & Test

Sohbete şu şekilde yazabilirsiniz:
> **/benim Taşınabilir Mini Termal Yazıcı (Mürekkepsiz cep yazıcısı, maliyet: $6, satış fiyatı: $29)**

Yapay zeka anında şu 5 adımlı raporu sunacaktır:
1. **Kazanan Ürün Skoru:** Problem çözme ve "Vay Canına" faktör puanı (88/100).
2. **Hedef Ülke:** Tier 1 (ABD, İngiltere, Avustralya) - Öğrenciler, planlayıcılar ve anneler için yüksek satın alma gücü.
3. **Reklam Mecrası:** TikTok Ads (1. Tercih - Görsel ürün) + Instagram Reels.
4. **Video Reklam Senaryosu:** 
   - *Hook (0-3 sn):* "Mürekkep kartuşlarına yüzlerce lira dökmeyi hemen bırakın..."
   - *Problem-Çözüm (4-15 sn):* Çantadan çıkarıp telefondan 2 saniyede fotoğraf/not basımı.
   - *CTA (23-30 sn):* "%50 İndirim + Ücretsiz Kargo".
5. **Birim Maliyet (Unit Economics):** Başa baş ROAS: 1.34x, Maksimum Harcanabilir CPA: $21.50.
