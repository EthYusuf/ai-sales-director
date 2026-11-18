#!/usr/bin/env node
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
// Initialize MCP Server
const server = new McpServer({
    name: "ecommerce-winning-product-hunter",
    version: "1.0.0",
});
/**
 * TOOL 1: analyze_product_viability
 * Evaluates whether a product is a high-potential winning product.
 */
server.tool("analyze_product_viability", "Analyzes an e-commerce product idea across 6 critical dimensions to determine if it is a 'Winning Product' for dropshipping/direct-to-consumer (D2C).", {
    productName: z.string().describe("Name of the product (e.g., 'Portable Lint Remover', 'Posture Corrector Bra', 'Mini Thermal Printer')"),
    category: z.string().describe("Product category (e.g., 'Beauty & Personal Care', 'Home & Kitchen', 'Pet Supplies', 'Tech Gadgets', 'Fitness')"),
    description: z.string().describe("Brief description of how the product works and what problem it solves"),
    targetPriceUSD: z.number().optional().describe("Intended selling price in USD (e.g., 29.99)"),
    costPriceUSD: z.number().optional().describe("Product supply cost including shipping from supplier in USD (e.g., 6.50)"),
    uniqueSellingPoint: z.string().optional().describe("What makes this product unique or viral"),
}, async ({ productName, category, description, targetPriceUSD, costPriceUSD, uniqueSellingPoint }) => {
    // Evaluation Logic
    const descLower = (description + " " + (uniqueSellingPoint || "") + " " + productName).toLowerCase();
    // 1. Problem Solving score
    let problemSolvingScore = 6;
    if (descLower.match(/(pain|save|clean|fix|reliev|protect|easy|fast|anti-|posture|headache|acne|sleep|dog|cat)/)) {
        problemSolvingScore = 9;
    }
    // 2. Wow / Scroll-Stopping factor
    let wowFactorScore = 5;
    if (descLower.match(/(magic|thermal|led|laser|auto|smart|foldable|invisible|instant|satisfying|before and after)/)) {
        wowFactorScore = 9;
    }
    else if (descLower.match(/(portable|mini|wireless|waterproof)/)) {
        wowFactorScore = 7;
    }
    // 3. Margin & Pricing Health
    let marginScore = 7;
    let marginRecommendation = "Ürünü en az 3x çarpanla satmanız tavsiye edilir (Maliyet x 3 = Satış Fiyatı).";
    if (targetPriceUSD && costPriceUSD) {
        const margin = ((targetPriceUSD - costPriceUSD) / targetPriceUSD) * 100;
        const multiplier = targetPriceUSD / (costPriceUSD || 1);
        if (multiplier >= 3.5 && margin >= 70) {
            marginScore = 10;
            marginRecommendation = `Harika marj! %${margin.toFixed(1)} brüt marj ve ${multiplier.toFixed(1)}x fiyat çarpanı reklam bütçesi için oldukça güvenli.`;
        }
        else if (multiplier >= 2.5 && margin >= 60) {
            marginScore = 7.5;
            marginRecommendation = `Makul marj (%${margin.toFixed(1)}). Reklam maliyetlerini optimize etmeniz veya Bundle (2'li alımda indirim) yapmanız gerekir.`;
        }
        else {
            marginScore = 4;
            marginRecommendation = `Düşük marj riski (%${margin.toFixed(1)}). Ücretli reklamlarda kâra geçmek zor olabilir, fiyatı artırın veya paket teklifleri ekleyin.`;
        }
    }
    // 4. Shipping & Fragility Risk
    let shippingRisk = "DÜŞÜK";
    let shippingNote = "Küçük, hafif ve kırılmaz görünüyor; uluslararası kargo hasar riski düşük.";
    if (descLower.match(/(glass|ceramic|liquid|battery|heavy|bulky|large|knife|blade)/)) {
        shippingRisk = "ORTA / YÜKSEK";
        shippingNote = "Kırılabilir cam, sıvı, batarya veya hacimli ürünler gümrükte takılabilir veya kargo maliyetini şişirebilir.";
    }
    // 5. Total Winning Score calculation
    const totalScore = Math.min(100, Math.round((problemSolvingScore * 3.5) + (wowFactorScore * 3.5) + (marginScore * 3)));
    let verdict = "🚀 YÜKSEK POTANSİYEL (KAZANAN ÜRÜN ADAYI)";
    let verdictColor = "GREEN";
    if (totalScore < 60) {
        verdict = "❌ DÜŞÜK POTANSİYEL / ZORLU PAZAR (Geliştirilmeli veya başka ürün seçilmeli)";
        verdictColor = "RED";
    }
    else if (totalScore < 75) {
        verdict = "⚠️ ORTA POTANSİYEL (Yalnızca doğru kanca ve spesifik bir niş hedefleme ile çalışır)";
        verdictColor = "YELLOW";
    }
    const report = {
        product: productName,
        category,
        overallWinningScore: `${totalScore}/100`,
        verdict,
        evaluationBreakdown: {
            problemSolvingScore: `${problemSolvingScore}/10`,
            wowFactorScore: `${wowFactorScore}/10`,
            marginAndPricingScore: `${marginScore}/10`,
            shippingAndReturnRisk: shippingRisk,
            shippingAssessment: shippingNote,
        },
        marginAnalysis: marginRecommendation,
        whyItWinsOrLoses: [
            problemSolvingScore >= 8 ? "✅ Gerçek ve acil bir problemi çözüyor (İnsanlar acıyı dindirmek için para harcar)." : "ℹ️ Problem çözmekten ziyade istek/hobi ürünü, duygusal tetikleyici gerektirir.",
            wowFactorScore >= 8 ? "✅ Videolarda ilk 3 saniyede izleyiciyi durduracak (Scroll-stopper) görsel etkiye sahip." : "ℹ️ Görsel olarak sıradan görünebilir, yaratıcı video senaryosu şart.",
            shippingRisk === "DÜŞÜK" ? "✅ Hafif ve dayanıklı, iade ve kırılma oranı düşük olacaktır." : "⚠️ Lojistik ve kargo test edilmeli, gümrük sınırlamalarına dikkat edilmeli."
        ],
        recommendedNextSteps: [
            "1. TikTok Creative Center ve Facebook Ad Library üzerinden rakiplerin en son aktif reklamlarını kontrol edin.",
            "2. Ürünü tek satmak yerine '1 Alana 1 Bedava' veya '2'li Aile Paketi %30 İndirim' gibi tekliflerle Ortalama Sepet Tutarını (AOV) yükseltin.",
            "3. recommend_target_countries aracıyla bu ürünün en kârlı satılacağı ülkeleri belirleyin.",
            "4. generate_ad_channel_strategy aracıyla reklam platformu ve video senaryolarını oluşturun."
        ]
    };
    return {
        content: [{ type: "text", text: JSON.stringify(report, null, 2) }]
    };
});
/**
 * TOOL 2: recommend_target_countries
 * Analyzes the best global markets for the given product.
 */
server.tool("recommend_target_countries", "Recommends the most profitable target countries and markets for an e-commerce product based on purchasing power, logistics, and consumer behavior.", {
    productName: z.string().describe("Name of the product"),
    category: z.string().describe("Category of the product"),
    priceRange: z.enum(["budget", "mid_ticket", "high_ticket"]).describe("Price range: budget ($15-$30), mid_ticket ($35-$75), high_ticket ($80+)"),
    nicheFocus: z.string().optional().describe("Specific sub-niche (e.g., 'Fitness lovers', 'Home chefs', 'Outdoor / camping', 'Office ergonomics')")
}, async ({ productName, category, priceRange, nicheFocus }) => {
    const analysis = {
        product: productName,
        category,
        priceTier: priceRange,
        niche: nicheFocus || "Genel Tüketici",
        tier1Markets: [
            {
                country: "Amerika Birleşik Devletleri (ABD)",
                code: "US",
                fitScore: "9.5/10",
                why: "Dünyanın en büyük e-ticaret pazarı. Dürtüsel satın alma (impulse buy) refleksi en yüksek ülke. Stripe ve yerel ödeme altyapıları kusursuz çalışır.",
                logistics: "YunExpress, CNE veya CJ Dropshipping ile 6-10 iş gününde teslimat mümkündür.",
                marketingNote: "Reklam CPM maliyetleri yüksektir ancak sepet tutarı (AOV) ve dönüşüm oranı çok kuvvetlidir."
            },
            {
                country: "Birleşik Krallık (İngiltere)",
                code: "GB",
                fitScore: "9.0/10",
                why: "Yüksek internetten alışveriş alışkanlığı. Coğrafi olarak kompakt olduğu için kargo teslimatları çok hızlı gerçekleşir.",
                logistics: "Royal Mail / Hermes entegre hatları ile 5-8 gün.",
                marketingNote: "£ (Pound) kurları kâr marjını yükseltir. 135 GBP altı vergi muafiyeti/IOSS kurallarına dikkat edilmelidir."
            },
            {
                country: "Kanada & Avustralya",
                code: "CA / AU",
                fitScore: "8.8/10",
                why: "ABD'ye kıyasla daha düşük reklam rekabeti (CPM) ve yüksek alım gücü.",
                logistics: "Avustralya ters mevsim avantajı sunar (Kuzey yarımküre kışken orada yazdır; sezonluk ürünler için müthiş bir yedek pazardır!)."
            },
            {
                country: "Almanya & Hollanda",
                code: "DE / NL",
                fitScore: "8.5/10",
                why: "Avrupa'nın en güçlü ekonomileri. Kaliteli ve problem çözen teknik ürünleri çok severler.",
                logistics: "DHL / Hermes. Almanca dil desteği ve yerel ödeme (Sofort, Klarna, iDeal) eklenirse dönüşüm %40 artar."
            }
        ],
        emergingHighMarginMarkets: [
            {
                region: "Körfez Ülkeleri (GCC: BAE, Suudi Arabistan, Kuveyt, Katar)",
                fitScore: priceRange === "high_ticket" || priceRange === "mid_ticket" ? "9.2/10" : "7.5/10",
                advantage: "Kişi başı inanılmaz yüksek harcama gücü. Lüks ve ilgi çekici ürünlere bayılırlar.",
                criticalFactor: "Kapıda Ödeme (Cash on Delivery - COD) bu bölgede çok popülerdir. BAE'de kredi kartı oranı yüksektir."
            }
        ],
        marketsToAvoidInitially: [
            "Hindistan, Brezilya, Nijerya (Yüksek gümrük vergileri, teslim edilmeme oranı ve düşük ödeme güveni nedeniyle başlangıçta dropshipping için önerilmez).",
            "İtalya & İspanya (Yalnızca yerelleştirilmiş dil ve kapıda ödeme opsiyonu varsa test edilmelidir, iade oranı yüksektir)."
        ],
        recommendedLaunchStrategy: [
            "Adım 1: İlk testi ABD pazarında yapın (en hızlı veri ABD'den toplanır).",
            "Adım 2: Kazanan reklam açısını bulduktan sonra İngiltere, Kanada ve Avustralya'ya yatay ölçekleme (horizontal scaling) yapın.",
            "Adım 3: Ürün sezonluksa mevsim geçişlerinde Avustralya ve Yeni Zelanda'yı hedefleyin."
        ]
    };
    return {
        content: [{ type: "text", text: JSON.stringify(analysis, null, 2) }]
    };
});
/**
 * TOOL 3: generate_ad_channel_strategy
 * Formulates the winning ad channel, creative script, and media budget breakdown.
 */
server.tool("generate_ad_channel_strategy", "Generates platform-specific marketing strategies (TikTok, Meta/Instagram, Google Ads, Pinterest) and high-converting video ad script frameworks.", {
    productName: z.string().describe("Name of the product"),
    targetAudience: z.string().describe("Target persona (e.g., 'Gen Z students', 'Mothers aged 25-45', 'Gym enthusiasts', 'Pet owners')"),
    productType: z.enum(["visual_gadget", "problem_solver", "fashion_beauty", "home_decor", "b2b_office"]).describe("Nature of the product"),
    budgetLevel: z.enum(["low_testing", "standard", "aggressive"]).describe("Starting daily test budget")
}, async ({ productName, targetAudience, productType, budgetLevel }) => {
    // Channel suitability
    const platformRankings = [];
    if (productType === "visual_gadget" || productType === "fashion_beauty") {
        platformRankings.push({
            platform: "TikTok Ads & TikTok Organik (UGC)",
            priority: "1. TERCİH (MUTLAKA YAPILMALI)",
            why: "Ürün görsel olarak dikkat çekici ve viral olma katsayısı yüksek. TikTok kullanıcıları eğlenirken alışveriş yapmaya çok açık.",
            recommendedAdFormat: "Spark Ads veya Whitelisted UGC Video Reklamı (Gerçek kullanıcı deneyimi gibi görünen dikey 9:16 videolar)."
        });
        platformRankings.push({
            platform: "Meta (Instagram Reels & Facebook Feed)",
            priority: "2. TERCİH",
            why: "25-55 yaş arası daha geniş ve satın alma gücü olgun kitleyi yakalamak için idealdir. Retargeting (yeniden hedefleme) için vazgeçilmezdir.",
            recommendedAdFormat: "Reels Video + Advantage+ Alışveriş Kampanyası (ASC)."
        });
    }
    else if (productType === "problem_solver") {
        platformRankings.push({
            platform: "Meta (Facebook Feed & Instagram Reels)",
            priority: "1. TERCİH (EN YÜKSEK DÖNÜŞÜM)",
            why: "Problem çözen ürünlerde Facebook'un 'Problem-Çözüm' video kurguları ve uzun metinli hikaye anlatımı olağanüstü yüksek ROAS getirir.",
            recommendedAdFormat: "Ağrıyı/Problemi gösteren ilk 3 saniyelik video + Fayda maddeleri + Müşteri yorumları overlay."
        });
        platformRankings.push({
            platform: "TikTok Ads",
            priority: "2. TERCİH",
            why: "'TikTok Made Me Buy It' formatında hızlı çözüm demonstrasyonları çok hızlı satar.",
            recommendedAdFormat: "POV / Hikaye anlatımlı gerçekçi video."
        });
        platformRankings.push({
            platform: "Google Search & Performance Max",
            priority: "3. TERCİH (ARAMA HACMİ VARSA)",
            why: "Eğer insanlar bu problemi doğrudan Google'da aratıyorsa (örn: 'bel ağrısı yastığı'), Google Ads yüksek niyetli (high intent) hazır alıcıları toplar.",
            recommendedAdFormat: "Google Shopping & Responsive Search Ads."
        });
    }
    else if (productType === "home_decor") {
        platformRankings.push({
            platform: "Pinterest Ads & Instagram",
            priority: "1. TERCİH",
            why: "Ev dekorasyonu, estetik ve hediye ürünlerinde Pinterest kullanıcılarının satın alma niyeti çok yüksektir (%70+ kadın kitle, yüksek gelir düzeyi).",
            recommendedAdFormat: "Estetik video pinler, oda içi atmosfer çekimleri, Before/After dönüşümleri."
        });
    }
    // Video Script Framework (UGC / Viral ad template)
    const videoScript = {
        targetAudience,
        structure: "3 Aşamalı Kazanan Video Kurgusu (Hook - Body - CTA)",
        hookOptions: [
            {
                second: "0:00 - 0:03 (Kanca / Hook)",
                text: `Eğer siz de [Yaygın Problem]'den bıktıysanız, bu videoyu geçmeyin!`,
                visual: "Kameraya doğrudan konuşma veya problemin yaşandığı anın dramatik, abartılı görüntüsü (Örn: sinirli bir yüz, dökülen bir şey, ağrı anı)."
            },
            {
                second: "0:00 - 0:03 (Merak Kancası)",
                text: `Amazon'da bunu bulana kadar hayatımın ne kadar zor olduğunu fark etmemiştim...`,
                visual: "Paket açılışı veya ürünün kutudan ilk çıktığı an."
            },
            {
                second: "0:00 - 0:03 (Karşılaştırma Kancası)",
                text: `Pahalı alternatiflere yüzlerce dolar ödemeyi hemen bırakın!`,
                visual: "Eski yöntem vs Yeni Ürün yan yana karşılaştırması."
            }
        ],
        bodySection: {
            second: "0:04 - 0:18 (Problem & Çözüm)",
            elements: [
                "1. Problemin ne kadar can sıkıcı olduğunu gösterin (1-2 saniye).",
                `2. ${productName} ürününü devreye sokun: Nasıl çalıştığını pratik şekilde gösterin.`,
                "3. 3 Temel Faydayı ekrana yazı (overlay captions) olarak ekleyin.",
                "4. Müşteri sosyal kanıtı: '50.000+ mutlu müşteri yanılıyor olamaz!'"
            ]
        },
        callToActionSection: {
            second: "0:19 - 0:25 (Harekete Geçirici Mesaj - CTA)",
            script: "Bugüne özel %50 indirim ve Ücretsiz Kargo fırsatını kaçırmayın. Profildeki linkten siparişinizi oluşturun!",
            visual: "İndirim kodu animasyonu, tükeniyor uyarısı (Urgency) ve 'Sipariş Ver' butonu gösterimi."
        }
    };
    // Budget Allocation
    let budgetPlan = {
        budgetLevel,
        dailyTestingBudget: budgetLevel === "low_testing" ? "$30 - $50 / Gün" : budgetLevel === "standard" ? "$75 - $150 / Gün" : "$200+ / Gün",
        recommendedSplit: [
            "70% Yeni Müşteri Edinimi (Cold Traffic / TOF - TikTok veya Meta ASC Kampanyası)",
            "20% Yaratıcı / Kreatif Testleri (Farklı Hook ve Video varyasyonları testi)",
            "10% Yeniden Hedefleme (Retargeting / BOF - Sepeti terk edenlere %10 kuponlu reklam)"
        ]
    };
    return {
        content: [{
                type: "text",
                text: JSON.stringify({
                    product: productName,
                    platformRecommendations: platformRankings,
                    videoAdScriptFormula: videoScript,
                    budgetDistributionPlan: budgetPlan
                }, null, 2)
            }]
    };
});
/**
 * TOOL 4: calculate_ecommerce_unit_economics
 * Calculates profitability, margins, break-even ROAS and maximum allowed CPA.
 */
server.tool("calculate_ecommerce_unit_economics", "Calculates critical e-commerce unit economics: Gross Profit, Net Margin, Break-even ROAS, and Maximum Allowable Acquisition Cost (CPA).", {
    sellingPriceUSD: z.number().describe("Customer retail price on your store"),
    productCostUSD: z.number().describe("Product manufacturing / supplier cost"),
    estimatedShippingUSD: z.number().default(0).describe("Shipping cost paid by you (0 if included in product cost or charged to customer)"),
    paymentGatewayFeePercent: z.number().default(3.5).describe("Stripe/PayPal fee percentage (typically 2.9% - 3.5%) + $0.30"),
    customMiscCostsUSD: z.number().default(1.0).describe("Packaging, customer service, chargeback reserve cushion per order")
}, async ({ sellingPriceUSD, productCostUSD, estimatedShippingUSD, paymentGatewayFeePercent, customMiscCostsUSD }) => {
    const totalCogs = productCostUSD + estimatedShippingUSD;
    const paymentFee = (sellingPriceUSD * (paymentGatewayFeePercent / 100)) + 0.30;
    const grossProfitBeforeAds = sellingPriceUSD - totalCogs - paymentFee - customMiscCostsUSD;
    const grossMarginPercent = (grossProfitBeforeAds / sellingPriceUSD) * 100;
    // Break-even CPA (The most you can pay for a purchase in ads without losing money)
    const breakEvenCPA = grossProfitBeforeAds;
    // Break-even ROAS = Selling Price / Break-even CPA
    const breakEvenROAS = sellingPriceUSD / (breakEvenCPA > 0 ? breakEvenCPA : 0.01);
    // Scenarios at different ROAS levels
    const scenario2_0_CPA = sellingPriceUSD / 2.0;
    const netProfitAtROAS_2 = grossProfitBeforeAds - scenario2_0_CPA;
    const scenario2_5_CPA = sellingPriceUSD / 2.5;
    const netProfitAtROAS_2_5 = grossProfitBeforeAds - scenario2_5_CPA;
    const scenario3_0_CPA = sellingPriceUSD / 3.0;
    const netProfitAtROAS_3 = grossProfitBeforeAds - scenario3_0_CPA;
    const calculation = {
        priceAndCostOverview: {
            retailPrice: `$${sellingPriceUSD.toFixed(2)}`,
            productAndShippingCOGS: `$${totalCogs.toFixed(2)}`,
            paymentGatewayFee: `$${paymentFee.toFixed(2)}`,
            miscReserve: `$${customMiscCostsUSD.toFixed(2)}`,
            grossProfitBeforeMarketing: `$${grossProfitBeforeAds.toFixed(2)}`,
            grossMargin: `%${grossMarginPercent.toFixed(1)}`
        },
        keyAdMetrics: {
            breakEvenROAS: `${breakEvenROAS.toFixed(2)}x (Reklamlarda bu ROAS'ın üzerinde olduğunuz her satış kârlıdır)`,
            maximumAllowableCPA: `$${breakEvenCPA.toFixed(2)} (Müşteri başına reklama ödeyebileceğiniz maksimum tutar)`
        },
        profitabilityProjectionsPer100Orders: {
            atROAS_2_0: {
                adSpend: `$${(scenario2_0_CPA * 100).toFixed(2)}`,
                revenue: `$${(sellingPriceUSD * 100).toFixed(2)}`,
                netProfit: `$${(netProfitAtROAS_2 * 100).toFixed(2)}`,
                netMarginPercent: `%${((netProfitAtROAS_2 / sellingPriceUSD) * 100).toFixed(1)}`
            },
            atROAS_2_5: {
                adSpend: `$${(scenario2_5_CPA * 100).toFixed(2)}`,
                revenue: `$${(sellingPriceUSD * 100).toFixed(2)}`,
                netProfit: `$${(netProfitAtROAS_2_5 * 100).toFixed(2)}`,
                netMarginPercent: `%${((netProfitAtROAS_2_5 / sellingPriceUSD) * 100).toFixed(1)}`
            },
            atROAS_3_0: {
                adSpend: `$${(scenario3_0_CPA * 100).toFixed(2)}`,
                revenue: `$${(sellingPriceUSD * 100).toFixed(2)}`,
                netProfit: `$${(netProfitAtROAS_3 * 100).toFixed(2)}`,
                netMarginPercent: `%${((netProfitAtROAS_3 / sellingPriceUSD) * 100).toFixed(1)}`
            }
        },
        expertRecommendation: grossMarginPercent >= 65
            ? "✅ Kârlılık yapısı çok sağlıklı. Rahatlıkla reklam testlerine başlayabilirsiniz."
            : "⚠️ Marj düşük kalmış! Sepet tutarını (AOV) artırmak için 2'li paket veya sepet aşamasında tek tıkla eklenen Upsell (Örn: Yedek başlık, garanti uzatma) ekleyin."
    };
    return {
        content: [{ type: "text", text: JSON.stringify(calculation, null, 2) }]
    };
});
/**
 * TOOL 5: get_ecommerce_playbook
 * Practical playbooks for competitor spying, scaling, and ad creative formats.
 */
server.tool("get_ecommerce_playbook", "Returns actionable master playbooks on competitor ad spying, creative hooks, scaling rules, and conversion rate optimization (CRO).", {
    topic: z.enum([
        "competitor_spy_methods",
        "winning_product_checklist",
        "creative_hook_vault",
        "scaling_playbook"
    ]).describe("Playbook topic to retrieve")
}, async ({ topic }) => {
    const playbooks = {
        competitor_spy_methods: {
            title: "E-Ticarette Rakipleri ve Kazanan Ürünleri Casuslama Rehberi",
            tactics: [
                {
                    method: "Meta Ad Library (Facebook Reklam Kütüphanesi)",
                    url: "https://www.facebook.com/ads/library",
                    howTo: "Niş anahtar kelimelerini yazın (örn: 'portable blender', '%50 OFF', 'free worldwide shipping'). Filtrelerden 'Tüm Reklamlar' ve 'Aktif' olanları seçin. Bir reklam 30 günden uzun süredir aktifse O REKLAM PARA BASIYORDUR."
                },
                {
                    method: "TikTok Creative Center (Top Ads Dashboard)",
                    url: "https://ads.tiktok.com/business/creativecenter/inspiration/topads",
                    howTo: "Bölgeyi 'United States', sektörü nişiniz olarak filtreleyin. Son 7 ve 30 günde en yüksek CTR ve beğeni alan reklamların video kurgularını inceleyin."
                },
                {
                    method: "TikTok Organic Search Hilesi",
                    howTo: "TikTok arama çubuğuna '#tiktokmademebuyit', '#viralproduct', 'unboxing [niş]' yazın. Filtrelerden 'Son 1 Ay' ve 'En Çok Beğenilenler'i seçin. Yorumlarda 'Where can I buy this?' (Nereden alabilirim?) yazan ürünleri tespit edin."
                }
            ]
        },
        winning_product_checklist: {
            title: "2026-2027 Kazanan Ürün 7 Altın Kuralı (The 7 Pillars)",
            rules: [
                "1. Net Bir Acıyı / Problemi Çözmeli: İnsanlar keyiften önce acıdan kurtulmak için hemen kartını çıkarır.",
                "2. 'Vay Canına' (Wow-Factor) Etkisi: İlk 3 saniyede parmak kaydırmayı durduran görsel bir çekicilik olmalı.",
                "3. Kolay Bulunamama (Not easily found in local retail): Müşteri ürünü yerel markette veya bakkalda bulamamalı.",
                "4. En Az 3x Fiyat Çarpanı: $10'a mal edip en az $30-$35'e satabilmelisiniz (Reklam maliyetlerini karşılamak için).",
                "5. Kolay ve Hafif Kargolanabilir: Ağırlığı 500 gramın altında olmalı, kırılabilir cam veya regülasyona tabi tehlikeli madde içermemeli.",
                "6. Geniş Hedef Kitle (Mass Market Appeal): Sadece 1.000 kişiye değil, milyonlarca insana hitap edebilmeli.",
                "7. Reklam ve İçerik Üretimine Uygunluk (UGC Friendly): Öncesi/Sonrası veya kullanım anı rahatça videoya çekilebilmeli."
            ]
        },
        creative_hook_vault: {
            title: "Yüksek Dönüşümlü İlk 3 Saniye Kancaları (Viral Ad Hooks)",
            hooks: [
                "Korku / FOMO: 'Bunu sipariş etmeden önce neden kimse beni uyarmadı?'",
                "Merak: 'Tiktok'ta 10 milyon izlenen bu gizli alet gerçekten işe yarıyor mu?'",
                "Dönüşüm / Karşılaştırma: 'Eski [Kötü Durum] vs Yeni [Harika Durum]'",
                "Hediye / İlişki: 'Eşime/Erkek arkadaşıma aldığım en iyi şey kesinlikle buydu...'",
                "Aykırı / Provokatif: 'Eğer hala [Eski Yöntem] yapıyorsanız, paranızı çöpe atıyorsunuz.'"
            ]
        },
        scaling_playbook: {
            title: "Reklam Ölçekleme Rehberi (Scaling Playbook)",
            rules: [
                "Dikey Ölçekleme (Vertical Scaling): Kârlı (ROAS > 2.5x) olan adset veya kampanyanın bütçesini her 24-48 saatte bir %20 artırın (Algoritmayı şoka sokmayın).",
                "Yatay Ölçekleme (Horizontal Scaling): Kazanan reklam kreatifinizi yeni ülkelere (İngiltere, Kanada, Avustralya, Almanya) açın.",
                "CBO / ASC Ölçekleme: En çok satan 3 kreatifinizi Meta Advantage+ Shopping Campaign (ASC) veya TikTok CBO içine koyarak yüksek bütçe verin.",
                "Kreatif Çeşitlendirme: Reklam yorulmasını (Creative Fatigue) önlemek için her hafta en az 3 yeni video kanca (Hook) varyasyonu ekleyin."
            ]
        }
    };
    return {
        content: [{ type: "text", text: JSON.stringify(playbooks[topic], null, 2) }]
    };
});
// Start Server via Stdio
async function run() {
    const transport = new StdioServerTransport();
    await server.connect(transport);
    console.error("Ecommerce Winning Product Hunter MCP Server running on stdio");
}
run().catch((error) => {
    console.error("Fatal error running MCP server:", error);
    process.exit(1);
});
