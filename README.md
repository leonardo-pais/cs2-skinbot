# CS2 SkinBot


![Python](https://img.shields.io/badge/python-3.13-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green)
![GitHub Repo Size](https://img.shields.io/github/repo-size/leonardo-pais/cs2-skinbot)

A lightweight bot that monitors **CS2 skin marketplaces** (CSFloat, DMarket(soon), Skinport(soon)) and sends **Discord notifications** when desired skins with specific float values are listed.

---

https://github.com/user-attachments/assets/7bd3c822-a251-4afe-bf8f-b8243663b29b

---

## 🚀 Features

- Monitor multiple CS2 marketplaces via public APIs  
- Filter skins by **name**, **float range**, and **price**  
- Send **real-time notifications** to a Discord channel  
- Fully configurable via `config.yaml`  
- Automatable with **GitHub Actions** or local scheduler  

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/leonardo-pais/cs2-skinbot
cd cs2-skinbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure secrets

- **Local development:** create a `.env` file

```bash
DISCORD_WEBHOOK=your_discord_webhook_url
CSFLOAT_API_KEY=your_csfloat_api_key
```

- **GitHub Actions:** add repository **Secrets**  
  - `DISCORD_WEBHOOK` → your Discord webhook URL  
  - `CSFLOAT_API_KEY` → your CSFloat API key  

---

### 4. Configure the bot

Edit `config.yaml`:

- `wanted_skins` → list of skins you want to track

Example:

```yaml
wanted_skins:
  - "AK-47 | Vulcan"
  - "Butterfly Knife | Fade"
  
sites:
  - name: "CSFloat"
    api_url: "https://csfloat.com/api/v1/listings"
    api_key: "${CSFLOAT_API_KEY}"
    query_params:
      limit: 20
      sort_by: "most_recent"
      min_float: 0.0009999
      max_float: 0.002
      category: 1
      type: buy_now
```

---

## 🏃 Usage

### Run locally

```bash
python main.py
```

### Run automatically with GitHub Actions

- Workflow file: `.github/workflows/skinbot.yml`  
- Scheduled to run **every 15 minutes**  
- Uses secrets for secure credentials  

---

## 💡 Contributing

- Open issues or pull requests for new marketplaces, features, or bug fixes  
- Keep secrets out of commits!  

---

## 📄 License

MIT License
