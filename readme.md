# HAI-Sentinel: GenAI Helpdesk Intelligence
**Developed by:** Harigovind (AI Scientist)
**Theme:** Wipro GenAI Challenge 2026

## 🌟 Overview
HAI-Sentinel is a high-performance, secure, and Gemini-inspired AI Helpdesk solution. It is designed to transform enterprise ticketing data into actionable insights using RAG (Retrieval-Augmented Generation) and high-speed inference.

## 🚀 Key Features
- **Gemini-Style UI:** A clean, minimal, and responsive interface optimized for both Desktop and Mobile.
- **RAG Integration:** The system "reads" uploaded documents (PDFs/Logs) and provides 100% accurate answers based on company data.
- **Mobile-Ready Commands:** Fully compatible with mobile browsers, supporting voice-to-text input commands.
- **Master Security Key:** Advanced PII masking (hiding emails/phones) and prompt injection protection to ensure data privacy.

## 🛠️ Technical Stack
- **AI Model:** Llama-3-8B (via Groq Cloud)
- **Vector DB:** ChromaDB (for fast document retrieval)
- **Backend:** FastAPI (High-speed API)
- **Frontend:** Streamlit (Modern UI)
- **Deployment:** Docker & Docker-Compose

## 📂 Project Structure
- `app/`: Contains the Brain (Engine), Security, and API logic.
- `frontend/`: Contains the Gemini-like user interface.
- `db/`: The storage area for uploaded helpdesk files.
- `docker-compose.yml`: One-click deployment script.

## 📝 How to Run
1. Add your `GROQ_API_KEY` in the `.env` file.
2. Place your helpdesk documents in the `db/` folder.
3. Run `docker-compose up --build`.
4. Access the UI at `localhost:8501`.
  
