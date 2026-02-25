# TuneAI 

TuneAI is an end-to-end music playlist platform that uses artificial intelligence to generate customized song selections from user-chosen genres. The project includes a modern and responsive interface developed with Vue 3 and Tailwind CSS, supported by a backend driven by a large language model to produce curated results.

![Project Preview](will add screenshot here)  
*(PREVIEW REMINDER)*

🌐 **Live Demo**  
[Explore the live demo](ega-web-app.vercel.app) *(LINK REMINDER)*

## 🚀 Features

- **AI-Powered Curation**: Instantly generates 5-song playlists using a large language model.

- **Modern UI/UX**: Clean, simple and fully responsive design.

- **Interactive Experience**: Real-time loading states and dynamic genre selection.

- **Robust Backend**: Efficient API with proper error handling and consistent JSON responses.

## 🛠️ Technology Stack

### Frontend
- Framework: **Vue 3** (Composition API)
- Language: **Javascript**
- Build Tool: **Vite**
- Styling: **Tailwind CSS**
- HTTP Client: **Axios**

### Backend
- Framework: **FastAPI** 
- Language: **Python 3.12**
- AI Provider: **Hugging Face Inference Router - DeepSeek model**
- Utilities: `python-dotenv`, `openai` SDK (OpenAI-compatible client)

## 📋 Prerequisites

- **Node.js** (v18 or higher)
- **Python** (v3.12 recommended)

## ⚙️ Installation & Setup

### 1. Backend Setup

```bash
# Navigate to the server directory
cd api

# Create virtual environment
python3 -m venv .venv

# Activate it
# Linux/macOS:
source .venv/bin/activate
# Windows:
.\.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

> Security Note: API keys are unavailable, see the `/api/.env.example` file for the naming syntax, then create the `.env` file and add your API key

### 2. Frontend Setup (Client)

Navigate to the cloned repository and install Node dependencies.

```bash
# Go to the frontend directory
cd frontend

# Install dependencies
npm install
```

---

## 🏃‍♂️ Running the Application

Two terminals running simultaneously are needed, one for the frontend server and one for the backend server.

### Terminal 1: Start the Backend
```bash
cd api
# Ensure venv is activated
python index.py
```
The server will start at `http://127.0.0.1:3000`.

### Terminal 2: Start the Frontend
```bash
cd frontend
npm run dev
```
The application will launch at `http://localhost:5173`.

---

## 🔌 API Documentation

### Generate Playlist
Generates a curated list of exactly 5 songs based on the provided genre.

- **Endpoint**: `POST /api/playlist_api`
- **Content-Type**: `application/json`
- **Request Body**:
  ```json
  {
    "genre": "pop"
  }
  ```
- **Success Response** (200 OK):
  ```json
  {"songs":
    [
      {"title":"Sicko Mode","artist":"Travis Scott"},{"title":"HUMBLE.","artist":"Kendrick Lamar"},{"title":"God's Plan","artist":"Drake"},{"title":"Juicy","artist":"The Notorious B.I.G."},{"title":"N.Y. State of Mind","artist":"Nas"}
    ]
  }
  ```

### Health Check
- **Endpoint**: `GET /api/health`
- **Response**: HEALTHY.

---

## 📂 Project Structure

```
kolade-oyeyipo/
├── api/                       # Backend FastAPI service
│   ├── .env.example           # Environment variables template
│   ├── index.py               # Main API entry point (FastAPI)
│   ├── playlist_api.py        # Playlist generation logic
│   └── requirements.txt       # Python dependencies
├── frontend/                  # Frontend Vue 3 application
│   ├── src/
│   │   ├── assets/            # Static assets
│   │   ├── components/        # Reusable Vue components
│   │   ├── router/            # Vue Router configuration
│   │   ├── views/             # Page views
│   │   ├── App.vue            # Root component
│   │   └── main.js            # Frontend entry point
│   ├── public/                # Public assets
│   ├── index.html             # HTML template
│   ├── package.json           # Node.js dependencies/scripts
│   ├── tailwind.config.js     # Tailwind CSS configuration
│   └── vite.config.js         # Vite configuration
├── vercel.json                # Vercel deployment configuration
└── README.md                  # Project documentation

Ignore this...