# Customer Service AI Agent – Frontend

A lightweight **Streamlit web interface** for the AI Customer Service Agent.
This frontend connects to the Flask backend and provides users with a simple, interactive chat experience.

> 💡 Works together with the [Backend Repo](https://github.com/MagdiWaleed/customer-service-backend).

---

## ✨ Features

* Chat with the AI Customer Service Agent in a clean web UI
* Multi-user support with conversation memory
* Service recommendations & enrollment flow
* Smooth integration with the backend API

---

## 📸 Demo

Amazon is just a **sample dataset** (not affiliated).
*(Insert GIF/screenshot of your demo here)*
[Watch the demo](https://youtu.be/R7gtjDmP00I)

---

## ⚙️ Installation

Clone the repo:

```bash
git clone https://github.com/MagdiWaleed/customer-service-frontend.git
cd customer-service-frontend
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run Chat.py
```

---

## 🔗 Backend Connection

Make sure the [backend](https://github.com/MagdiWaleed/customer-service-backend) is running, and update the API URL in the frontend code if needed:

```python
BACKEND_URL = "http://127.0.0.1:5000"   # or your deployed backend URL
```

---

## 🛠 Tech Stack

* **Frontend** → Streamlit
* **Backend** → Flask (via REST API)
* **AI/ML** → Powered by LlamaIndex, LangChain, LangGraph (in backend)
* **Language** → Python
---

## 📂 Project Structure

```
.
├── Chat.py                  # Main Streamlit frontend app
├── pages/                  # Authentication page
├── requirements.txt
└── README.md
```

---

## 🚀 Future Improvements

* Add authentication & user profiles
* Improve UI/UX with richer components
* Add support for multiple backend endpoints
* Deploy as a hosted web app (Streamlit Cloud / Docker)

---

## 📬 Contact

If you find this project useful, feel free to ⭐ star the repo and connect on [LinkedIn](www.linkedin.com/in/magdi-waleed).
