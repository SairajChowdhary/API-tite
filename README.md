# API-tite
An AI-powered food discovery app that recommends specific dishes based on your unique taste profile, built with Python, Flask, and NLTK.

# 🚀 API-tite

Welcome to **API-tite** – your all-in-one toolkit for effortless API development, testing, and documentation!  
Whether you're a backend wizard or just starting your API journey, API-tite streamlines every step.

---

## 🎬 Animated Overview

![API-tite Animation](https://github.com/SairajChowdhary/API-tite/assets/1018115666/animated-demo.gif)

---

## 🧩 Features

- **Plug & Play API Endpoints**
- **Auto-generated Docs**
- **Live Testing Playground**
- **Secure Authentication**  
- **Performance Analytics**

---

## 🛠️ Technologies

![Tech Stack](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95.2-green?logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-6.0-green?logo=mongodb)
![Docker](https://img.shields.io/badge/Docker-ready-blue?logo=docker)

---

## 🖼️ Infographics

### **API-tite Architecture**

![API-tite Architecture](https://github.com/SairajChowdhary/API-tite/assets/1018115666/architecture-diagram.svg)

---

### **How It Works**

```mermaid
graph TD
    A[Developer] -->|Creates| B(API-tite)
    B --> C{Endpoints}
    C --> D[Docs]
    C --> E[Playground]
    C --> F[Analytics]
    F --> G[Performance Dashboard]
```

---

## 🚦 Quick Start

```bash
git clone https://github.com/SairajChowdhary/API-tite.git
cd API-tite
docker-compose up --build
```
Your API is live at `http://localhost:8000`!

---

## 🤝 Contributing

We love contributors!  
Check out [`CONTRIBUTING.md`](CONTRIBUTING.md) for how to get started.

---

## 📬 Contact

Questions? Feedback?  
[Open an issue](https://github.com/SairajChowdhary/API-tite/issues) or email [SairajChowdhary](mailto:sairajchowdhary@gmail.com).

---

> _API-tite: The bite-sized API toolkit with a big impact!_

---

### 🎨 More Visuals

#### System Flow

![System Flow](https://github.com/SairajChowdhary/API-tite/assets/1018115666/system-flow.png)

#### Live Usage Stats

![Live Usage Stats]((https://substack-post-media.s3.amazonaws.com/public/images/3eedbbd4-e0a4-4519-be5c-ee0c644df55f_1280x1502.gif))

---

<!-- Animation and diagrams created using [LottieFiles](https://lottiefiles.com/) and [Mermaid](https://mermaid-js.github.io/). Replace demo links/images with your own if preferred. -->
I Built this using Flask to serve recommendations and manage data, making the system modular and scalable.
You can do API testing using Postman or simply use curl
So basically you can run this following the below steps:
- git clone https://github.com/your-username/API-tite.git
- cd API-tite
-- pip install -r requirements.txt or pip3 install -r requirements.txt
 # run the Flask application
-- Run 'python3 app.py' in your terminal and then send a POST request to the /setup endpoint using a tool like Postman or curl

you should see this in your terminal:
 * Serving Flask app 'app'
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
And Leave this terminal window open! This is your running server. If you close it, the next step will fail.
# Terminal 2: Set Up the Database
Open a new terminal and paste this:
curl -X POST http://127.0.0.1:5000/setup
you should see: {"message":"Database setup complete."}
This basically created a new file named 'gourmetgo.db'. That's a SQLite database with sample data.
Happy Coding!
        ~Sairaj Chowdhary
