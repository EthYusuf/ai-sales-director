# 🚀 AI Sales Director (MCP Server & Universal Skill)
### Model Context Protocol (MCP) Server for E-Commerce Winning Product Discovery, Global Market Fit & Viral Ad Strategy

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![MCP Protocol](https://img.shields.io/badge/MCP-1.6.0-green.svg)](https://modelcontextprotocol.io/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.7-blue)](https://www.typescriptlang.org/)
[![Node.js Version](https://img.shields.io/badge/node-%3E%3D20.0.0-brightgreen)](https://nodejs.org/)
[![Multi-Platform](https://img.shields.io/badge/Supported-Antigravity%20%7C%20Claude%20%7C%20Cursor%20%7C%20ChatGPT-orange)](#-cross-platform-support)

> **Stop burning cash on products that won't sell.**  
> **AI Sales Director** (`/sales-manager`) is an enterprise-grade AI skill and MCP Server engineered to evaluate e-commerce and dropshipping products before spending a single dollar on ads. It tells you **if a product will win**, **which countries will buy it most**, **which ad platform to prioritize (TikTok vs Meta vs Google)**, and **the exact break-even ROAS required**.

---

## ⚡ What It Solves

E-commerce entrepreneurs often launch products based on gut feeling, burning thousands on ad spend only to discover:
- The product lacks visual "scroll-stopping" appeal.
- Shipping and supplier costs destroy profit margins.
- Ads were launched on the wrong platform (e.g. Meta instead of TikTok, or Google instead of Pinterest).
- They targeted high-chargeback or high-customs regions.

**AI Sales Director solves this with institutional unit economics and market intelligence.**

---

## 🛠️ MCP Server Tools

The MCP Server exposes 5 high-precision tools compliant with the **Model Context Protocol (MCP)**:

| Tool Name | Description | Key Output |
| :--- | :--- | :--- |
| `analyze_product_viability` | Evaluates 6 core dimensions across the 7 Pillars of winning products. | 0-100 Score, Problem Utility, Wow-Factor, Risk Assessment. |
| `recommend_target_countries` | Analyzes purchasing power, logistics lines, and payment culture. | Tier 1 (US/UK/CA/AU), GCC (UAE/KSA), Avoidance list. |
| `generate_ad_channel_strategy`| Determines optimal ad platform & builds 30s viral ad scripts. | TikTok vs Meta vs Google breakdown, 3-Second Hooks, CTA. |
| `calculate_ecommerce_unit_economics` | Simulates COGS, landed freight, and gateway fees. | Gross Margin, Break-even ROAS, Maximum Allowable CPA. |
| `get_ecommerce_playbook` | Actionable intelligence from top dropshipping operators. | Competitor spying guides (Ad Library, TikTok Creative Center). |

---

## 🏗️ Architecture & Cross-Platform Support

```text
                               +-----------------------------+
                               |     AI Client Interface     |
                               |  Claude | Cursor | Gemini   |
                               | ChatGPT | Antigravity | CLI |
                               +--------------+--------------+
                                              |
                                     [/sales-manager]
                                              |
                       +----------------------+----------------------+
                       |                                             |
            +----------v-----------+                     +-----------v----------+
            |  Standard Prompt     |                     |  Universal MCP SDK   |
            |  Offline Execution   |                     |  Stdio JSON-RPC      |
            +----------------------+                     +-----------+----------+
                                                                     |
                                             +-----------------------+-----------------------+
                                             |                       |                       |
                                   +---------v---------+   +---------v---------+   +---------v---------+
                                   | Product Viability |   | Target Market Fit |   | Unit Economics    |
                                   | 7 Pillars (0-100) |   | Tier 1 & GCC Maps |   | Break-even ROAS   |
                                   +-------------------+   +-------------------+   +-------------------+
```

Compatible across all major modern AI ecosystems:
- **Google Antigravity & Gemini CLI:** Pre-configured via `.gemini/skills/sales-manager/SKILL.md`
- **Claude Code & Claude Desktop:** Configured via `.claude/commands/sales-manager.md` & `claude_desktop_config.json`
- **Cursor IDE & Windsurf:** Enabled via `.cursorrules` and `cursor_mcp.json`
- **OpenAI ChatGPT / Custom GPTs / Codex:** Configured via `chatgpt_custom_gpt_instructions.txt`

---

## 🚀 Quick Start & Installation

### Option 1: Standalone Node.js MCP Server

1. **Clone the repository:**
   ```bash
   git clone https://github.com/EthYusuf/ai-sales-director.git
   cd ai-sales-director/mcp-server
   ```
2. **Install dependencies & build:**
   ```bash
   npm install
   npm run build
   ```
3. **Start the server:**
   ```bash
   npm start
   ```

### Option 2: Add to Claude Desktop

Add this snippet to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "sales-manager": {
      "command": "node",
      "args": [
        "<PATH_TO_REPO>/mcp-server/dist/index.js"
      ]
    }
  }
}
```

### Option 3: Add to Cursor IDE

Go to **Cursor Settings** -> **Features** -> **MCP Servers** -> **Add New MCP Server**:
- **Name:** `sales-manager`
- **Type:** `command`
- **Command:** `node <PATH_TO_REPO>/mcp-server/dist/index.js`

---

## 💡 How to Use: `/sales-manager`

Once installed, simply type in your AI prompt:

```text
/sales-manager Portable Mini Thermal Printer (Inkless pocket printer, supply cost: $6.50, selling price: $29.99)
```

### Sample Institutional Report:

```markdown
1. 🚀 WINNING PRODUCT VIABILITY: 88/100 (HIGH POTENTIAL)
   - Problem-Solving Utility: 8/10 (No messy, expensive ink cartridges)
   - Scroll-Stopping Wow Factor: 9/10 (Instant black & white printing via phone)
   - Logistics Risk: LOW (Under 200g, non-fragile)

2. 🌍 TARGET GLOBAL MARKETS
   - Tier 1: USA, UK, Canada, Australia (Students, journal lovers, busy mothers)
   - Emerging GCC: UAE & Saudi Arabia (High demand for aesthetic smart gadgets)
   - Note: Launch first in the US, horizontally scale to Australia & UK.

3. 📱 AD PLATFORM & VIDEO STRATEGY
   - Priority 1: TikTok Ads & Organic UGC (Visual demonstration creates instant impulse buy)
   - Priority 2: Meta (Instagram Reels) for 25-45 age group
   - 3-Second Hook: "Stop wasting $60 on printer ink cartridges! Watch this..."
   - Structure: Problem Agitation -> Instant Solution Demonstration -> Limited Offer CTA

4. 💰 UNIT ECONOMICS
   - Retail Price: $29.99
   - Landed Supply Cost: $6.50
   - Gateway & Misc Fees: $1.35
   - Gross Margin: 73.8% ($22.14 profit before ads)
   - Break-Even ROAS: 1.35x (Profitable at any ROAS above 1.35x)
   - Max Allowable CPA: $22.14
```

---

## 🇹🇷 Türkçe Özet

Bu proje; e-ticaret ve dropshipping yapan girişimcilerin doğru ürünü bulmasını, doğru ülkede satmasını ve doğru platformda (TikTok / Meta / Google) reklam vermesini sağlayan profesyonel bir **Yapay Zeka Satış Müdürü (AI Sales Director)** sistemidir. `/sales-manager` veya `/benim` komutuyla çalışır. Detaylı Türkçe rehber için [KULLANIM_KILAVUZU.md](file:///c:/Users/yusuf/OneDrive/Desktop/printtomoney/autormaiton/KULLANIM_KILAVUZU.md) dosyasını inceleyebilirsiniz.

---

## 📄 License

Distributed under the MIT License. Feel free to use, modify, and distribute.
Authored by [EthYusuf](https://github.com/EthYusuf).
