# 🔮 Sangoma Locator App

A secure and feature-rich online consultation platform that connects **Sangomas (traditional healers)** with **Patients**, enabling video, voice, and chat consultations using an in-app coin system. The app ensures privacy, identity verification, and secure payments — all while promoting African spirituality, philosophy, and numerology.

Live Demo(https://vundla.github.io/sangoma-locator-app/)
---

## 🚀 Features

### 🧑‍⚕️ User Types
- **Sangoma**: Registers by uploading ID and bank statement, approved by Admin.
- **Patient**: Registers with ID and bank statement, approved by Admin.

### ✅ Admin Approval System
- All accounts must be approved by the Admin before becoming active.

### 💰 Coin-Based Billing System
- Buy coins using **Visa**, **Capitec Pay**, or **voucher codes (OTT, 1Voucher)**.
- R100 = 1,000 coins, R200 = 2,000 coins ... up to R10,000 = 100,000 coins.
- Deducted per action:
  - 📩 Text Message: 25 coins per message
  - 📞 Voice Call: 150 coins per minute (cost doubles every minute)
  - 🎥 Video Call: 300 coins per minute (cost doubles every minute)

### 💬 Communication
  - **In-app messaging** only — no email, number, or banking info sharing.
  - Supports:
  - Real-time Chat
  - Secure Voice Calls
  - Secure Video Calls
  - Limits:
  - Max 48 Sangomas
  - Max 200 Patients per day

### 🤖 YAMI – Your AI Multicultural Intelligence

Our built-in AI chatbot **YAMI** (Your AI Multicultural Intelligence) is trained to guide and assist patients with:

- 🔮 African Spirituality
- 📜 African Philosophy
- ✝️ Christianity
- 🔢 Numerology
- 💭 Dream Interpretation
- 🧭 Sangoma Recommendations

YAMI acts as a 24/7 assistant for users needing spiritual guidance before speaking with a Sangoma. It ensures users are directed to the highest-rated Sangomas based on past consultations.

 
  

### 🌟 Sangoma Rating & Perks
- Patients rate Sangomas after sessions.
- Top-rated Sangomas earn ⭐ stars monthly.
- After 12 months of 5/5 ratings:
- 50% coin discount
- Access to patient phone numbers (privilege-only)

---

## 🛠️ Tech Stack

- **Python** (Flask)
- **SQLite** (Database)
- **HTML/CSS** (Frontend)
- **JavaScript + WebRTC** (Voice/Video calls)
- **Flask-SQLAlchemy**
- **Payment Integration**: Capitec Pay, Visa, OTT/1Voucher

---

## 📂 Project Structure



sangoma-locator-app/
├── app/
│ ├── init.py
│ ├── routes/
│ │ ├── auth.py
│ │ ├── chat.py
│ │ ├── call.py
│ │ ├── coins.py
│ │ └── ai.py
│ ├── utils/
│ └── models.py
├── run.py
├── config.py
├── requirements.txt
└── README.md


